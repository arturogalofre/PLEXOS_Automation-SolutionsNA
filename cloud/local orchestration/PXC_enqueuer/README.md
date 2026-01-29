# PLEXOS Cloud Enqueuer

A utility tool to automate the submission of PLEXOS models to PLEXOS Cloud (PXC).

## 1. Features
- **Study Sync**: Automatically syncs a local PLEXOS XML to a PLEXOS Cloud Study.
- **Flexible Model Selection**: Choose models interactively, via a config file, or from `config.csv`.
- **Smart Enqueuing**: Fetches machine recommendations (CPU/RAM) based on previous runs or falls back to defaults.
- **Engine Selection**: Automatically uses the latest available PLEXOS Engine.

## 2. Prerequisites
- **PLEXOS Cloud CLI (`pxc`)** installed and authenticated.
- **PLEXOS Desktop API** installed (for local XML parsing).
- **Python 3.x** and `pandas` library.

## 3. Usage

1. **Configure**: Edit `config.csv` to set defaults.
   - `studyId`: "show studies" (interactive), a specific ID, or path to a local XML.
   - `models`: "show models" (interactive), "models.csv", or specific names.
   - `vm_type`: Default VM size (e.g., "4-32") if no recommendation exists.
  
2. **Run**:
   ```bash
   python submit_to_PLEXOS_Cloud.py
   ```

3. **Interact**: Follow the terminal prompts to select your study and models if not hardcoded.

## 4. File Structure
- `submit_to_PLEXOS_Cloud.py`: Main script.
- `config.csv`: Configuration settings.
- `stubs.py`: Helper for loading PLEXOS API assemblies.


## 5. PLEXOS Cloud JSON job definition

```json
{
  "StudyId": "<STUDY_GUID>",
  "ChangeSetId": "<CHANGESET_GUID>",
  "Models": [
    "<MODEL_NAME>"
  ],
  "SimulationOptions": {
    "Locale": 1033,
    "EnableRealTimeLog": false,
    "IsModelDistributionRun": false,
    "SolutionOptions": {
      "ParquetSchemaVersion": 2
    },
    "SimulationTasks": [
      {
        "Name": "<TASK_NAME>",
        "TaskType": "Pre",
        "Arguments": "<COMMAND_TO_RUN>",
        "ContinueOnError": true,
        "ExecutionOrder": 1,
        "Files": [
          {
            "Path": "<RELATIVE_PATH_OR_GLOB>",
            "Version": null
          }
        ]
      },
      {
        "Name": "<TASK_NAME>",
        "TaskType": "Post",
        "Arguments": "<COMMAND_TO_RUN>",
        "ContinueOnError": true,
        "ExecutionOrder": 2
      }
    ]
  },
  "ParallelizationOptions": {
    "InstanceCount": 1
  },
  "SimulationData": [
    {
      "Uri": "<CHANGESET_DATABASE_URI>",
      "Type": "ChangesetDatabase"
    },
    {
      "Uri": "<TIMESERIES_URI>",
      "Type": "TimeseriesZipped"
    }
  ],
  "SimulationEngine": {
    "EngineId": "<ENGINE_GUID>",
    "Version": "<PLEXOS_VERSION>",
    "EngineType": "Standard",
    "OperatingSystem": 1,
    "OptimizationEngine": 0
  },
  "Source": "<CLI|SDK|Jupyter>",
  "Priority": 1,
  "RequestedCpuCores": 4,
  "MinimumMemoryInGb": 16,
  "SimulationType": "None"
}

```

### `StudyId`

**Type:** `string (GUID)`
Identifies the PLEXOS **Study** in Cloud.

* All simulations run within a study context
* Used to locate input data, results, and metadata

This value must match an existing study in PLEXOS Cloud.

---

### `ChangeSetId`

**Type:** `string (GUID)`
Specifies the **changeset** applied to the study.

* Represents a versioned snapshot of the database
* Determines which inputs are used for the run
* Often maps to scenario or revision logic

---

### `Models`

**Type:** `array[string]`
List of model names to run within the study.

* Usually contains a single model
* Must match the model name exactly as defined in the study
* Supports multi-model studies

---

## `SimulationOptions`

Controls **runtime behavior**, logging, tasks, and solution output.

### `Locale`

**Type:** `integer`
Sets the locale for the simulation environment.

* `1033` = English (US)
* Affects formatting, logging, and regional settings

---

### `EnableRealTimeLog`

**Type:** `boolean`
Enables real-time logging from the VM.

* Useful for debugging long or complex runs
* Logs stream while the job is executing

---

### `IsModelDistributionRun`

**Type:** `boolean`
Indicates whether this is a distributed model run.

* Typically `false` for standard simulations
* Used in advanced distribution workflows

---

### `SolutionOptions`

Controls **solution output format**.

#### `ParquetSchemaVersion`

**Type:** `integer`
Defines the Parquet schema used for solution outputs.

* Version `2` is the current standard
* Affects downstream post-processing compatibility

---

## `SimulationTasks`

Defines **pre-processing and post-processing scripts** executed on the VM.

Each task is executed **inside the same VM** as the simulation.

### Common Task Fields

#### `Name`

Human-readable description of the task.

#### `TaskType`

**Values:** `Pre` | `Post`

* `Pre` runs **before** the PLEXOS engine
* `Post` runs **after** the solution is complete

#### `Arguments`

Command executed on the VM.

* Usually a Python invocation
* Runs in the synced working directory

#### `ContinueOnError`

**Type:** `boolean`

* `true` → simulation continues even if the task fails
* `false` → job fails immediately on error

#### `ExecutionOrder`

**Type:** `integer`

Defines execution order among tasks.

* Lower numbers run first
* Allows chaining multiple pre or post tasks

---

### Example: Pre-Processing Task

* Writes membership data to disk
* Runs before the simulation starts
* Syncs files from `simulation/**`

---

### Example: Post-Processing Task

* Configures DuckDB query views
* Runs after the solution is complete
* Used for structured result access

---

## `ParallelizationOptions`

Controls **horizontal scaling**.

### `InstanceCount`

**Type:** `integer`

* Number of parallel instances to run
* Commonly `1` for deterministic runs
* Higher values used for scenario sweeps

---

## `SimulationData`

Defines **input data sources** pulled into the VM.

Each entry includes:

### `Uri`

Cloud endpoint for downloading input data.

### `Type`

Specifies the data category.

Common values:

* `ChangesetDatabase`
* `TimeseriesZipped`

These are synced to the VM before execution begins.

---

## `SimulationEngine`

Defines the **PLEXOS engine configuration**.

### `EngineId`

Unique identifier for the engine build.

### `Version`

Exact PLEXOS version used.

* Ensures reproducibility
* Critical for debugging differences across runs

### `EngineType`

Typically `Standard`.

### `OperatingSystem`

* `1` usually indicates Linux

### `OptimizationEngine`

Selects the solver backend.

---

## Execution Metadata

### `Source`

Indicates where the job was submitted from.

Examples:

* `CLI`
* `SDK`
* `Jupyter`

---

### `Priority`

**Type:** `integer`

* Higher priority jobs may start sooner
* Subject to account limits

---

### `RequestedCpuCores`

Number of CPU cores allocated to the VM.

* Must align with model size
* Over-requesting may increase queue time

---

### `MinimumMemoryInGb`

Minimum RAM required for the job.

* Ensures large models do not OOM
* VM will not start unless this is met

---

### `SimulationType`

Used for advanced or custom workflows.

* `None` for standard simulations

  

---

## Practical Notes

* All pre/post scripts must exist in Datahub before submission
* File paths are relative to the synced working directory
* VM environment is ephemeral, Datahub is the persistence layer
* Engine version mismatches are a common source of issues

---

## Typical Use Cases

* Automated database inspection before runs
* Result normalization and extraction
* Batch studies with consistent pre/post logic
* Fully reproducible cloud workflows
