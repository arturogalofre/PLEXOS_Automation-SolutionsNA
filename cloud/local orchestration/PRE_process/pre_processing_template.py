"""
PLEXOS Cloud Pre-Processing Script Template
-------------------------------------------
Use this template to create your own pre-processing logic.
This script runs BEFORE the simulation engine starts.

What it does:
1. Connects to the input PLEXOS database (reference.db).
2. Allows you to run SQL queries to inspect or modify data.
3. Saves reports or logs to the output folder for you to download later.

How to use:
1. Look for sections marked [USER EDITABLE].
2. Add your own SQL queries.
3. detailed logic to write your own CSV or Markdown files.
"""
''''''
import duckdb
import os
import pandas as pd
from datetime import datetime
import sys

# ==========================================
# SECTION 1: CONFIGURATION & PATHS
# ==========================================
# These environment variables are automatically set by PLEXOS Cloud.
# We interpret them here so your script knows where to look.
print("--- Starting Pre-Processing Script ---")

# 'simulation_path' is where your input files (XML/DB) live.
SIMULATION_PATH = os.environ.get('simulation_path', "/simulation")

# 'output_path' is where you must save anything you want to keep.
OUTPUT_PATH = os.environ.get('output_path', "/output")

# The PLEXOS XML is converted to this SQLite file before your script runs.
DATABASE_FILE = os.path.join(SIMULATION_PATH, "reference.db")

print(f"Reading inputs from: {SIMULATION_PATH}")
print(f"Writing outputs to:  {OUTPUT_PATH}")

# ==========================================
# SECTION 2: HELPER FUNCTIONS
# ==========================================
def save_to_csv(df, filename):
    """Ref Helper: Saves a pandas DataFrame to the output folder."""
    if df is None or df.empty:
        print(f"Warning: Dataframe for {filename} is empty. Skipping.")
        return
    
    full_path = os.path.join(OUTPUT_PATH, filename)
    df.to_csv(full_path, index=False)
    print(f"Saved: {full_path}")

# ==========================================
# SECTION 3: MAIN LOGIC
# ==========================================
def main():
    # Ensure output directory exists (good practice for local testing)
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    try:
        # 3.1 CONNECT TO DATABASE
        # We use DuckDB to read the SQLite file efficiently.
        with duckdb.connect() as con:
            print("Initializing database connection...")
            con.execute("INSTALL sqlite;")
            con.execute("LOAD sqlite;")
            
            # Check if DB exists before attaching
            if not os.path.exists(DATABASE_FILE):
                raise FileNotFoundError(f"Database not found at: {DATABASE_FILE}")

            # Attach the PLEXOS input database as 'reference'
            con.execute(f"ATTACH '{DATABASE_FILE}' AS reference (TYPE SQLITE);")
            con.execute("USE reference;")

            # ---------------------------------------------------------
            # [USER EDITABLE] SECTION 3.2: YOUR CUSTOM QUERIES
            # ---------------------------------------------------------
            print("Running custom queries...")

            # EXAMPLE 1: Count all objects in the model
            # This is a simple query to check the size of the model.
            count_sql = "SELECT COUNT(*) FROM t_object"
            model_size = con.execute(count_sql).fetchone()[0]
            print(f"Total objects in model: {model_size}")

            # EXAMPLE 2: Extract specific data (e.g., Generator Names)
            # You can write any SQL here. Tables are t_object, t_class, t_membership, t_data, etc.
            gen_query = """
                SELECT o.Name AS GeneratorName, c.Name AS ClassName
                FROM t_object o
                JOIN t_class c ON o.class_id = c.class_id
                WHERE c.Name = 'Generator'
                LIMIT 10
            """
            # Fetch result as a Pandas DataFrame
            generators_df = con.execute(gen_query).fetchdf()

            # ---------------------------------------------------------
            # [USER EDITABLE] SECTION 3.3: SAVE OUTPUTS
            # ---------------------------------------------------------
            print("Saving outputs...")

            # Save the dataframe we created above
            save_to_csv(generators_df, "preview_generators.csv")

            # Create a simple generic log file
            log_path = os.path.join(OUTPUT_PATH, "script_status.txt")
            with open(log_path, "w") as f:
                f.write(f"Script ran successfully at {datetime.utcnow()}\n")
                f.write(f"Model Size (Objects): {model_size}\n")
            print(f"Log written to: {log_path}")

            print("--- Pre-Processing Complete ---")

    except Exception as e:
        # ==========================================
        # SECTION 4: ERROR HANDLING
        # ==========================================
        print("\n!!! ERROR OCCURRED !!!")
        print(str(e))
        # We re-raise the exception so PLEXOS Cloud knows the job failed.
        # If we swallow the error, the simulation might continue with bad data.
        sys.exit(1)

if __name__ == "__main__":
    main()
