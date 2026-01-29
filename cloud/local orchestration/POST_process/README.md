# PLEXOS Cloud Post-Processing

This directory contains scripts and tools for processing PLEXOS simulation results within the PLEXOS Cloud execution environment.

## 📂 Contents

* **`configure_duck2.py`**: A Python script to configure DuckDB views for PLEXOS solution files (Parquet format). It automates the creation of views for easy querying and exports specific data to CSV.
* **`VM_ENVIRONMENT.md`**: Detailed documentation of the Linux VM environment where these scripts run. **Read this before specific script development.**

## 🛠 `configure_duck2.py`

This script is designed to run in the post-processing phase of a PLEXOS Cloud simulation.

### Features
* Reads paths from `directorymapping.json`.
* Scans output directories for Parquet files.
* Creates DuckDB views for each data folder.
* Ensures critical views like `fullkeyinfo` and `data` exist.
* Exports "Regional Generation Capacity" (ChildClassName) data to CSVs in the output folder.

### Usage

```bash
python configure_duck2.py [ModelName] [Verbose]
```

* **ModelName**: (Optional) Name of the model in the mapping file. Defaults to internal constant if not provided.
* **Verbose**: (Optional) Set to `true` or `1` for detailed logs.

### Environment Variables
The script relies on the standard VM environment variables (see `VM_ENVIRONMENT.md`):
* `duck_db_path`: Default `/output/solution_views.ddb`
* `directory_map_path`: Default `/simulation/directorymapping.json`
* `csv_output_dir`: Directory for CSV exports.
* `child_classes_filter`: Comma-separated list to filter specific classes for export.

## ⚠️ Important Rules for Contributors

When modifying these scripts, remember the constraints of the execution environment:
1. **Absolute Paths**: Inputs are always in `/simulation`, outputs in `/output`.
2. **Tools**: Use `duckdb` for data interaction; `sqlite3` is not available.
3. **OS**: The environment is Ubuntu Linux (case-sensitive paths).

Refer to `VM_ENVIRONMENT.md` for a complete reference.


## How to create your own post processing scripts

Post processing scripts use the solution files created by the plexos simulations to create with them whatewver might be useful for the user. Examples for this can be processed data that is easier to analyse, data that can be used as an input for a new process and much else.

The solution data is organised in Parquet files that are the ones which will be queried to create the data we need.