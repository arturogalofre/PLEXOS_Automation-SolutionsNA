# VM Structure and Operation Guide

Based on the exploratory commands found in `Post_Simulation.log`, this document outlines the directory structure, file organization, and operational details of the Virtual Machine (VM) used for the simulation.

## Directory Structure Overview

The environment is organized into a specific hierarchy under the `/simulation` (or root `.`) directory.

### 1. Root Directory
The root contains the primary project definitions, databases, and immediate output logs.

*   **Project Files:**
    *   `project.xml`: The main PLEXOS project configuration file.
    *   `reference.db`: Reference database.
    *   `UpdatedBlankXML.db`: An updated database file likely used for the simulation.
*   **Scripts:**
    *   `query_write_memberships.py`: A Python script used to query or write membership data.
*   **Outputs & Logs:**
    *   `Output.xml`: The primary simulation output file (approx. 7.7 MB).
    *   `Pre_Simulation.log`, `Post_Simulation.log`, `Summary.log`: Logs capturing different stages of the execution.
    *   `PLXClient_...log`: Client-side logging for the PLEXOS execution.
    *   `Agent_Metrics.csv`: Metrics related to the agent's performance.

### 2. Model Nodal Solution (`/Model Nodal Solution`)
This directory holds the detailed results of the "Model Nodal" simulation run.

*   **Execution Info:**
    *   `Model ( Nodal ) Log.txt`: The specific log file for the nodal model run.
    *   `runstats.json`: JSON file containing runtime statistics.
    *   `iterfile.csv`, `stepfile.csv`, `summfile.csv`: CSV files tracking iterations and steps of the solver.
*   **Data Storage (`/version2`):**
    *   Contains a structured **Parquet** file system for storing large-scale solution data efficiently.
    *   **Structure:**
        *   `ParquetUploads/`: The main container for parquet data.
        *   **Subdirectories:** Organized by data entity type, such as `aggregatedseries`, `attribute`, `data` (contains the bulk data), `period`, `phase`, `property`, `unit`, etc.
        *   **Purpose:** This structure allows for fast querying and analysis of specific parts of the solution (e.g., just looking at `Unit` data or `Period` definitions) without loading the entire dataset.

### 3. Output Directory (`/Output`)
A dedicated folder for specific exported data.
*   `memberships_data.csv`: CSV data regarding memberships.
*   `metadata.datahub.csv`: Metadata info linking files to DataHub versions.

### 4. PLEXOS Configuration (`/PLEXOS`)
Contains low-level configuration and registry files for the PLEXOS engine.
*   `EE_reg.xml` & `EE_reg_interface.xml`: Registry and interface definitions.

### 5. Logs (`/logs`)
General system or application-level logs.
*   `log-2025-09-15.txt`: Timestamped execution log.
*   `study_map.json`: Mapping file for the study (currently empty).

### 6. App Data (`/app_data`)
Application specific data.
*   `PLEXOS Cloud/plexos-cloud.lcl`: Local configuration file for PLEXOS Cloud connectivity.

---

## Operational Workflow

Based on the file presence and timestamps, the typical operation flow within this VM is:

1.  **Setup:** The `project.xml` and necessary `.db` files (`UpdatedBlankXML.db`) are staged in the root.
2.  **Execution:** The PLEXOS engine runs, likely invoked via a script that uses `query_write_memberships.py` for setup or post-processing.
3.  **Solving:** The solver generates intermediate status files (`stepfile.csv`, `iterfile.csv`) in `Model Nodal Solution`.
4.  **Output Generation:**
    *   A full `Output.xml` is generated in the root.
    *   Detailed results are processed into the `version2` Parquet structure for high-performance access.
    *   Logs (`Model ( Nodal ) Log.txt`, `Post_Simulation.log`) are written to capture the process.
5.  **Data Versioning:** The `metadata.datahub.csv` is updated to track the versions of the output files (`Output.xml`, databases) relative to the central DataHub.

## Key Files for Debugging

*   **If the simulation failed:** Check `Model ( Nodal ) Log.txt` and `Pre_Simulation.log`.
*   **To analyze results:** Look at `Output.xml` for general results or query the Parquet files in `Model Nodal Solution/version2/ParquetUploads` for large-scale data analysis.
*   **To check connectivity/setup:** Review `plexos-cloud.lcl` and `PLXClient_...log`.
