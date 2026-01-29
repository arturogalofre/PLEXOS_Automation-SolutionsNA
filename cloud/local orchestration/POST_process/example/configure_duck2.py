import os
import sys
import json
import re
from pathlib import Path
import duckdb as duckdb

print("Post-Processing task running successfully!")

# Default model name (temporary override) – can be overridden by first CLI arg
DEFAULT_MODEL_NAME = "RT Energy 2024 Discounted_20240101"

def read_path_from_mapping_file(mapping_file_path: str, model_name: str) -> str:
    """
    Read the ParquetPath for the given model_name from the mapping file.
    Args:
        mapping_file_path (str): The path to the mapping file.
        model_name (str): The name of the model to search for.
    Returns:
        str: The ParquetPath for the given model_name, or None if not found.
    """
    with open(mapping_file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            if item.get('Name') == model_name:
                return item.get('ParquetPath')

def find_subdirectories(root_dir: str) -> list[str]:
    """
    Find all subdirectories of the given root directory.
    Args:
        root_dir (str): The root directory to search in.
    Returns:
        list[str]: A list of all subdirectories.
    """
    subdirectories = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            subdirectories.append(os.path.join(dirpath, dirname))
    return subdirectories

def _sanitize_filename(name: str) -> str:
    """Sanitize a class name into a safe filename fragment."""
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", name.strip())
    return cleaned or "unknown"


def configure_duck_views(model_name: str, verbose_log: bool = False) -> None:
    """
    Configure DUCK views for the given model_name.
    Args:
        model_name (str): The name of the model to configure views for.
        verbose_log (bool, optional): Whether to print verbose log messages. Defaults to False.
    """
    try:
        duckFilePath: str = os.environ.get('duck_db_path', "/output/solution_views.ddb")
        print(f'Setting up DUCK Views - using {duckFilePath}')
        
        mapping_file_path = os.environ.get('directory_map_path', "/simulation/directorymapping.json")
        model_directory = read_path_from_mapping_file(mapping_file_path, model_name)
        # model_directory = r"C:\Users\arturo.galofre\Documents\PrePost\AgentSolution\AgentSolutions9\Parquet"
        if model_directory is None:
            raise Exception(f"Unable to find output for model name provided {model_name}")
        else:
            print(f"Solution data found for {model_name}: {model_directory}")
        directories = find_subdirectories(model_directory)
        
        with duckdb.connect(duckFilePath) as con:
            # Create views for each subdirectory
            for item in directories:
                # Build a relative identifier-friendly name
                rel = os.path.relpath(item, model_directory).strip("./\\")
                # Skip nested data folders like data/dataFileId=0 which produce illegal view names (with '=')
                if 'dataFileId=' in rel:
                    if verbose_log:
                        print(f"[SKIP] Nested data segment '{rel}'")
                    continue
                # Drop empty or root
                if not rel:
                    continue
                # Flatten separators to underscores for safer view names
                view_name = re.sub(r"[^A-Za-z0-9_]+", "_", rel)
                path = os.path.join(item, "**", "*.parquet")
                view_command = f"CREATE OR REPLACE VIEW {view_name} AS SELECT * FROM '{path}'"  # no trailing semicolon needed
                try:
                    if verbose_log:
                        print(f"[VIEW] {view_command}")
                    con.execute(view_command)
                    if verbose_log:
                        try:
                            con.sql(f"select * from {view_name} limit 2").show()
                        except Exception as e:
                            print(f"[WARN] Preview for {view_name} failed: {e}")
                except Exception as e:
                    print(f"[ERROR] Failed to create view {view_name}: {e}")
                    raise

            # Ensure critical views exist (fullkeyinfo & data) even if directory naming differs
            # Attempt fallback direct glob if views missing
            existing_views = {r[0] for r in con.execute("SELECT table_name FROM information_schema.tables WHERE table_type='VIEW'").fetchall()}
            if 'fullkeyinfo' not in existing_views:
                fk_pattern = os.path.join(model_directory, 'fullkeyinfo', '*.parquet')
                con.execute(f"CREATE OR REPLACE VIEW fullkeyinfo AS SELECT * FROM '{fk_pattern}'")
            if 'data' not in existing_views:
                data_pattern = os.path.join(model_directory, 'data', '**', '*.parquet')
                con.execute(f"CREATE OR REPLACE VIEW data AS SELECT * FROM '{data_pattern}'")

            # Determine output directory for per-class CSV exports
            output_dir = os.environ.get('csv_output_dir') or os.path.dirname(duckFilePath) or '.'
            Path(output_dir).mkdir(parents=True, exist_ok=True)

            # Optional filter list (comma-separated) to limit classes
            filter_classes_env = os.environ.get('child_classes_filter')
            filter_classes = None
            if filter_classes_env:
                filter_classes = {c.strip() for c in filter_classes_env.split(',') if c.strip()}

            # Get distinct ChildClassName candidates
            try:
                child_classes = [r[0] for r in con.execute(
                    """
                    SELECT DISTINCT ChildClassName
                    FROM fullkeyinfo
                    WHERE ChildClassName IS NOT NULL AND ChildClassName <> ''
                    ORDER BY 1
                    """
                ).fetchall()]
            except Exception as e:
                print(f"[ERROR] Unable to read distinct ChildClassName values: {e}")
                child_classes = []

            if filter_classes:
                child_classes = [c for c in child_classes if c in filter_classes]

            if not child_classes:
                print("No ChildClassName values found to export.")
                return

            print(f"Exporting per-class CSV files to: {output_dir}")

            # Join to period to expose StartDate / EndDate in output
            base_query_template = (
                "SELECT key.*, d.PeriodId, p.StartDate AS PeriodStartDate, p.EndDate AS PeriodEndDate, d.Value "
                "FROM fullkeyinfo AS key "
                "INNER JOIN data d ON d.SeriesId = key.SeriesId "
                "INNER JOIN period p ON p.PeriodId = d.PeriodId "
                "WHERE key.PeriodTypeName = 'Interval' AND key.PhaseName = 'ST' "
                "AND key.ParentClassName = 'System' AND key.ChildClassName = ?"
            )

            for child_class in child_classes:
                sanitized = _sanitize_filename(child_class)
                target_csv = os.path.join(output_dir, f"{sanitized}_regional_generation_capacity.csv")
                if verbose_log:
                    print(f"[EXPORT] ChildClassName='{child_class}' -> {target_csv}")
                # Use parameter binding to avoid injection issues
                try:
                    # DuckDB COPY doesn't support parameter binding directly inside, so build safe literal
                    safe_literal = child_class.replace("'", "''")
                    export_sql = (
                        "COPY (" +
                        base_query_template.replace("?", f"'{safe_literal}'") +
                        f") TO '{target_csv}' (HEADER, DELIMITER ',')"
                    )
                    con.execute(export_sql)
                except Exception as e:
                    print(f"[ERROR] Export failed for {child_class}: {e}")
            print(f"Completed exports for {len(child_classes)} classes.")
    except Exception as e:
        print('Configuring DUCK Views failed due to an exception:')
        print(e)

if __name__ == "__main__":
    print("Starting configure_duck2.py")
    try:
        # Use CLI arg if provided, otherwise fall back to default constant
        if len(sys.argv) > 1:
            model_name = sys.argv[1]
        else:
            model_name = DEFAULT_MODEL_NAME
            print(f"[INFO] No model name argument supplied; using default: '{model_name}'")
        verbose_log = len(sys.argv) > 2 and sys.argv[2].lower() in ['1', 'true']
        configure_duck_views(model_name, verbose_log)
    except ValueError as e:
        print('Configuring duck views failed:')
        print(e)
    finally:
        print("done")