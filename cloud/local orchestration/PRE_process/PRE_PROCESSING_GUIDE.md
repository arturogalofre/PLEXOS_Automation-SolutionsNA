# PLEXOS Cloud Pre-Processing Guide

This guide explains how to create pre-processing scripts for PLEXOS Cloud simulations. These scripts run **before** the main simulation engine starts, allowing you to validate data, modify the input database, or generate summary reports.

---

## 1. The Environment (The "Black Box")

When a simulation job starts in the cloud, it spins up a temporary Virtual Machine (VM) or container to initialize the job.

### File Structure
The script processes files in specific locations defined by environment variables. Your script does not need to know the exact path on the Cloud server, as long as it uses these variables:

*   **Input (`SIMULATION_PATH`):** This folder contains your input data.
    *   **Crucial File:** `reference.db` (This is your PLEXOS XML converted into a SQLite database).
    *   [TODO: Add description of other expected input files, e.g., csvs, if applicable]
*   **Output (`OUTPUT_PATH`):** Any file you want to keep must be saved here.
    *   PLEXOS Cloud will zip everything in this folder and make it available as "Pre-Processing Logs" or "Output" after the job finishes.
*   **System Specs:**
    *   The environment runs Python [TODO: Insert Python Version, e.g., 3.10].
    *   Installed Libraries: `duckdb`, `pandas`, `os`, `sys`, `json`. [TODO: Verify list of available libraries]

---

## 2. The Standard Template

Use this boilerplate code to start any new pre-processing script. It handles the path configuration and database connection for you.

```python
import duckdb
import os
import pandas as pd
from datetime import datetime

# --- 1. SETUP PATHS ---
# We use environment variables to find where PLEXOS put the files.
# The defaults ("/simulation", "/output") work for local testing if you mimic the folder structure.
SIMULATION_PATH = os.environ.get('simulation_path', "/simulation")
OUTPUT_PATH = os.environ.get('output_path', "/output")

DB_FILE = os.path.join(SIMULATION_PATH, "reference.db") # The PLEXOS input database

print(f"Starting Pre-Processing...")
print(f"Reading from: {SIMULATION_PATH}")
print(f"Writing to:   {OUTPUT_PATH}")

def main():
    try:
        # --- 2. CONNECT TO DATABASE ---
        # We use DuckDB to read the SQLite file because it represents the input XML 
        # as a relational database.
        with duckdb.connect() as con:
            con.execute("INSTALL sqlite;")
            con.execute("LOAD sqlite;")
            
            # Attach the PLEXOS input file
            print(f"Attaching database: {DB_FILE}")
            con.execute(f"ATTACH '{DB_FILE}' AS reference (TYPE SQLITE);")
            con.execute("USE reference;")

            # --- 3. YOUR CUSTOM LOGIC GOES HERE ---
            # (See Section 3 below for how to write queries)
            
            # Example: Count total objects
            count = con.execute("SELECT COUNT(*) FROM t_object").fetchone()[0]
            print(f"Total objects in system: {count}")

            # --- 4. EXPORT RESULTS ---
            # Anything written to specific files in OUTPUT_PATH will be visible in the Cloud.
            
            # Example: Write a simple log file
            log_file = os.path.join(OUTPUT_PATH, "preprocessing_log.txt")
            with open(log_file, "w") as f:
                f.write(f"Pre-processing completed at {datetime.now()}\n")
                f.write(f"Total Objects Found: {count}\n")
            
            print(f"Log written to {log_file}")

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        # Raising an error ensures the PLEXOS job is marked as failed if this script fails
        raise e 

if __name__ == "__main__":
    main()
```

---

## 3. Writing Custom Queries

The PLEXOS XML structure is flattened into a Relational Schema (SQLite) inside `reference.db`. To extract data, you need to query these standard tables:

### Key Tables
| Table Name | Description |
| :--- | :--- |
| `t_object` | Contains every named item in your model (Generators, Nodes, Lines). |
| `t_class` | Defines the type of object (e.g., 'Generator', 'Node'). |
| `t_collection` | Defines the relationship types (e.g., 'Generators.Fuels'). |
| `t_membership` | Links Parent Objects to Child Objects (The actual topology). |
| `t_property` | Definitions of input properties (Max Capacity, Load, etc.). |
| `t_data` | The actual input values (numbers) associated with properties and objects. |

### Example Query: "Find all connections"
To see what connects to what (Memberships), you usually need to join `t_membership` with `t_object` twice (once for parent, once for child).

```python
# Inside the 'with duckdb.connect() as con:' block:

query = """
    SELECT 
        parent.Name AS ParentName,
        child.Name  AS ChildName,
        col.Name    AS CollectionName
    FROM t_membership m
    JOIN t_object parent ON m.parent_object_id = parent.object_id
    JOIN t_object child  ON m.child_object_id  = child.object_id
    JOIN t_collection col ON m.collection_id   = col.collection_id
    LIMIT 10
"""

# Fetch result as a Pandas DataFrame
df = con.execute(query).fetchdf()
print(df)
```

---

## 4. Saving Outputs

You cannot simply `print()` results if you want to save them for analysis. You must write files to the **`OUTPUT_PATH`**.

### Common Output Formats
1.  **Markdown Reports (`.md`):** Great for "System Overviews" that render nicely in the browser.
2.  **CSV Files (`.csv`):** Good for data exported for further analysis.
3.  **Flag Files:** Empty files used simply to signal that a step occurred.

### Code Example
```python
# Saving a DataFrame to CSV in the output folder
csv_path = os.path.join(OUTPUT_PATH, "my_custom_report.csv")
df.to_csv(csv_path, index=False)
```

---

## 5. Troubleshooting

If your script fails in the cloud:
1.  Check the **Log** tab in PLEXOS Cloud. It captures everything you `print()`.
2.  Ensure you aren't referencing hardcoded paths (e.g., `C:\Users\...`). Always use `os.path.join(SIMULATION_PATH, ...)`.
3.  Ensure your SQL query is valid for DuckDB/SQLite.
