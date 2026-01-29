# VM / Simulation Environment

This document describes the **Linux-based simulation VM** environment used for running PLEXOS simulations in the cloud. It is containerized and follows a strict directory and environment-variable convention. Use this context when writing or debugging scripts for this environment.

## 1. Operating System & Execution Context

* **Operating System:** Ubuntu Linux
* **Kernel:** `6.8.0-1031-azure` (Azure-hosted VM)
* **Architecture:** `x86_64` (64-bit)
* **User:** `root`
* **Current Working Directory:** `/simulation`

**Context:**
* You have full permissions.
* Paths are absolute and predictable.
* You are running inside a container layered on top of a host filesystem.

## 2. Core Directory Layout

### `/simulation` (PRIMARY INPUT WORKSPACE)
The **main working directory** where all simulation inputs live.
* **Contents:**
  * `project.xml`: Main simulation model definition (~6.8 MB)
  * `reference.db`: SQLite database used by the simulation (~7.6 MB)
  * `directorymapping.json`: Maps logical names (Simulation, Output) to physical paths
  * `auth.txt`: Authentication/config file (do not modify)
  * `Pre_Simulation.log`: Grows as scripts execute
* **Subdirectories:**
  * `Output/` → empty (legacy / not primary)
  * `app_data/PLEXOS Cloud/`: Contains `plexos-cloud.lcl` (local CLI configuration)
  * `logs/`: Execution logs, Study maps, Version metadata
  * `solution-archives/` → empty
  * `temp/` → empty

**Rule:** Treat `/simulation` as **read-only inputs + logs**, except where explicitly writing logs.

### `/output` (PRIMARY OUTPUT DIRECTORY)
* **Purpose:** Designated location for simulation results, generated outputs, and CLI logs.
* **Rule:** Anything produced by your code or simulation goes here.

### `/usr/local/bin`
* Contains executable binaries.
* **Key executable:** `plexos-cloud` (PLEXOS Cloud CLI)

## 3. Directory Mapping Logic

The file `/simulation/directorymapping.json` defines logical → physical path mappings:
```json
[
  {"Name": "Simulation", "Path": "/simulation", "Id": "<simulation_id>"},
  {"Name": "Output", "Path": "/output"}
]
```
**Implication:**
* Always refer to inputs via `/simulation`.
* Always write outputs via `/output`.

## 4. Environment Variables (CRITICAL)

Key environment variables are already set:
* `simulation_path = /simulation`
* `output_path = /output`
* `xml_input_path = /eedatadrive/EE/Sim/a/project.xml`
* `sqlite_input_path = /eedatadrive/EE/Sim/a/reference.db`
* `EE_CLI_LOGGING_PATH = /output`
* `PX_CLI_PATH = /usr/local/bin/plexos-cloud`
* `cloud_cli_path = /usr/local/bin/plexos-cloud`

**Best Practice:**
Robust scripts should access paths via environment variables with defaults:
```python
os.environ.get("simulation_path", "/simulation")
os.environ.get("output_path", "/output")
```

## 5. Storage & Mounts

* **Disk Device:** `/dev/sdc1` (XFS, ~1.1 TB, ~1 TB free)
* **Mount Points:** `/simulation`, `/output`
* **Root Filesystem:** `overlay` (Containerized)

**Implications:**
* Disk space is effectively unlimited.
* Input and output live on the same physical disk; reads/writes are fast.

## 6. Available Tools & Constraints

### CLI Tools
* ✅ **`plexos-cloud`**: The **only supported PLEXOS CLI** (at `/usr/local/bin/plexos-cloud`).
* ❌ **`pxc`**: Not installed. Do not use.

### Databases
* `reference.db` is **SQLite**.
* ❌ **`sqlite3` CLI**: Not installed.
* ✅ **Alternatives**: Use DuckDB (via Python or `duckdb` CLI).
* **Rule:** Query SQLite files via DuckDB, not sqlite3.

### Logs
* Located in `/simulation/logs`.
* CLI logging output goes to `/output`.

## 7. Operational Rules Summary

1. **Inputs live in:** `/simulation`
2. **Outputs must go to:** `/output`
3. **Use only:** `plexos-cloud` CLI
4. **Do not rely on:** `pxc` or `sqlite3`
5. **Use DuckDB** for database inspection
6. **Disk space is abundant**
7. **Python path assumptions** should match the VM (Linux)

## 8. Safe Exploration Commands

```bash
pwd
ls -alh /simulation
ls -alh /output
cat /simulation/directorymapping.json
head -n 50 /simulation/project.xml
/usr/local/bin/plexos-cloud --version
```
