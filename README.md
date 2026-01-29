# Energy Exemplar Automation Repository

Welcome to the centralized automation repository for Energy Exemplar. This repository serves as the single source of truth for our internal scripts, tools, and automation workflows.

## 📂 Repository Structure

The repository is organized to separate concerns and make it easy to find specific types of automation.

### `automation/`
The core automation scripts and projects, organized by domain.
- **`plexos/`**: Automation specific to PLEXOS simulation (e.g., input generation, execution, output extraction).
- **`aurora/`**: Automation specific to Aurora simulation.
- **`infrastructure/`**: Scripts for cloud resources (Azure/AWS), CI/CD pipelines, and server management.
- **`data_processing/`**: General ETL jobs, data cleaning scripts, and reporting tools not tied to a specific simulation engine.

### `shared_libraries/`
Reusable code modules to prevent duplication.
- **`python/`**: Common Python modules (e.g., logging wrappers, database connectors, API clients).
- **`powershell/`**: Common PowerShell modules and utility functions.

### `docs/`
Documentation for the repository and standards.
- **`guides/`**: "How-to" guides for running scripts and setting up environments.
- **`standards/`**: Coding standards, naming conventions, and contribution guidelines.

### `templates/`
Boilerplate code for starting new automation tasks.
- **`new_project/`**: Standard structure for a new automation tool.

### `tests/`
Unit and integration tests for the shared libraries and critical automation scripts.

## 🚀 Getting Started

1. **Clone the repository**: `git clone <repo-url>`
2. **Review the standards**: Check `docs/standards` before contributing.
3. **Explore**: Look into `automation/` to specific tools.

## 🤝 Contributing

We welcome contributions! Please follow the workflow:
1. Create a branch for your feature or fix.
2. Use the `templates/` to start new scripts.
3. Submit a Pull Request for review.
