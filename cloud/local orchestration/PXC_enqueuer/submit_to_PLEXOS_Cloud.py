# submit_to_PLEXOS_Cloud.py

import os
import sys
import logging
import subprocess
import json
import pandas as pd
from datetime import datetime
from stubs import DatabaseCore # Import PLEXOS modules directly from stubs

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set paths and load config
script_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(script_dir, 'config.csv')
config = pd.read_csv(config_path).fillna('')

# Helper functions
def get_config_value(assumption, default=None):
    """
    Retrieves a configuration value from config.csv based on the assumption key.
    
    Args:
        assumption (str): The assumption key to look up in the config.
        default (str): Default value to return if the key is not found in config.
    
    Returns:
        str: The configuration value if found, otherwise the default value.
    """
    try:
        value = config[config['assumption'] == assumption]['value'].reset_index(drop=True).values[0]
        # If value is empty or zero, use the default specified in the config
        if not value:
            value = config[config['assumption'] == assumption]['default'].reset_index(drop=True).values[0]
        return value if value else default
    except IndexError:
        # Log a warning and return the default value if the assumption is not found
        logging.warning(f"Assumption '{assumption}' not found in config.csv. Using default: {default}")
        return default
    
def update_config_file(key, value):
    config.loc[config['assumption'] == key, 'value'] = value
    config.to_csv(config_path, index=False)

# Flexible Study ID Handling
def get_study_id():
    study_id = get_config_value('studyId')
    if study_id.lower() == 'show studies':
        study_list_output = subprocess.check_output(["pxc", "study", "list", "--filterForCurrentUser"], shell=True, text=True)
        study_list = json.loads(study_list_output)
        print("Available Studies:")
        for idx, study in enumerate(study_list, start=1):
            print(f"{idx}. {study['Name']} (ID: {study['Id']})")
        study_number = int(input("Enter the number of the study you want to choose: "))
        study_id = study_list[study_number - 1]['Id']
        if input("Save this study ID? (y/n): ").strip().lower() == 'y':
            update_config_file('studyId', study_id)
    elif os.path.exists(study_id):
        sync_model_to_cloud(study_id)
    return study_id

# Function to execute CLI commands using subprocess
def run_cli_command(command_args):
    """
    Executes a CLI command using subprocess and captures the output.

    Args:
        command_args (list): List of command arguments.

    Returns:
        dict: Dictionary containing 'success', 'output', and 'error'.
    """
    try:
        logging.info(f"Executing command: {' '.join(command_args)}")
        result = subprocess.run(
            command_args,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        logging.debug(f"Command Output:\n{result.stdout}")
        if result.stderr:
            logging.debug(f"Command Error Output:\n{result.stderr}")
        return {
            "success": True,
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with return code {e.returncode}")
        logging.error(f"Error Output:\n{e.stderr}")
        return {
            "success": False,
            "output": e.stdout.strip() if e.stdout else "",
            "error": e.stderr.strip()
        }

def sync_model_to_cloud(study_id, plexos_xml_path):
    """
    Sync the PLEXOS XML model to the Cloud by creating or updating a study.

    Args:
        study_id (str): Study ID if it already exists.
        plexos_xml_path (str): Path to the PLEXOS XML file.

    Returns:
        str: Updated or new study ID.
    """
    try:
        # Determine if the provided study_id is a path or an ID
        if os.path.exists(study_id):
            plexos_xml_path = study_id
            study_name = os.path.basename(plexos_xml_path).replace(".xml", "")
            study_id = None
        else:
            study_name = None  # Use study_id directly if not a path

        # Step 1: Check if study already exists
        if not study_id:
            find_command = [
                "pxc", "study", "find", "--studyName", study_name, "--format", "json",
                "--filterForCurrentUser"
            ]
            find_response = run_cli_command(find_command)
            
            # Parse the JSON response if successful
            if find_response["success"]:
                try:
                    studies = json.loads(find_response["output"])
                    if studies:
                        existing_study_id = studies[0].get('Id')
                        logging.info(f"Found existing study with ID: {existing_study_id}")
                        return existing_study_id
                except json.JSONDecodeError:
                    logging.error("Failed to parse find study JSON response.")
                    raise
            else:
                logging.info("No matching study found, proceeding to create a new study.")

        # Step 2: Create a new study if no matching study ID is found
        if not study_id:
            create_command = [
                "pxc", "study", "create", "--name", study_name,
                "--database", plexos_xml_path, "--format", "json"
            ]
            create_response = run_cli_command(create_command)

            # Parse JSON output for successful study creation
            if create_response["success"]:
                try:
                    study_data = json.loads(create_response["output"])
                    new_study_id = study_data.get('Id')
                    if new_study_id:
                        logging.info(f"Created new study with ID: {new_study_id}")
                        return new_study_id
                except json.JSONDecodeError:
                    logging.error("Failed to parse create study JSON response.")
                    raise
            else:
                logging.error(f"Failed to create study: {create_response['error']}")
                raise Exception("Study creation failed.")
        
        # Step 3: Verify the given study ID with the user's accessible studies
        else:
            list_command = [
                "pxc", "study", "list", "--format", "json", "--filterForCurrentUser"
            ]
            list_response = run_cli_command(list_command)

            # Check if the given study_id exists in the list
            if list_response["success"]:
                try:
                    studies = json.loads(list_response["output"])
                    if any(study.get("Id") == study_id for study in studies):
                        logging.info(f"Successfully validated study ID: {study_id}")
                        return study_id
                    else:
                        logging.error("Provided study ID does not exist or is not accessible to the user.")
                        raise Exception("Invalid study ID.")
                except json.JSONDecodeError:
                    logging.error("Failed to parse study list JSON response.")
                    raise

    except Exception as e:
        logging.error(f"Error syncing model to cloud: {e}")
        raise

def setup_database_connection(file_path):
    """
    Set up the database connection to the PLEXOS dataset.
    
    Args:
        file_path (str): Path to the PLEXOS XML file.
    
    Returns:
        DatabaseCore: An instance of the DatabaseCore class with an open connection.
    """
    # Ensure file exists and adjust file path format if necessary

    # Adjusting the file path to avoid issues with backslashes
    file_path = file_path.strip('"').replace('\\', '/')

    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"Unable to locate the PLEXOS XML file: {file_path}")
    
    db = DatabaseCore()
    db.DisplayAlerts = False
    try:
        db.Connection(file_path)
        logging.info("Connected to PLEXOS dataset.")
    except Exception as e:
        logging.error(f"Failed to connect to PLEXOS dataset: {e}")
        raise
    return db

# Fetch model objects based on config.csv setting
def fetch_model_objects(plexos_xml_path):
    """
    Fetch model objects based on 'models' setting in config.csv.
    - 'show models': Connect to PLEXOS XML, list available models, and allow user selection.
    - 'use models.csv': Read models from models.csv file.
    - Specific model name(s): Use provided name(s) directly.
    """
    models_option = get_config_value('models', 'show models')
    
    if models_option == 'show models':
        # Connect to PLEXOS XML to retrieve all available models
        db = setup_database_connection(plexos_xml_path)
        try:
            class_ids = db.FetchAllClassIds()
            model_class_id = next((class_ids[key] for key in class_ids.Keys if key.lower() == 'model'), None)
            if not model_class_id:
                logging.error("The 'Model' class was not found in the PLEXOS dataset.")
                return []
            model_objects = db.GetObjects(model_class_id)
            model_names = list(model_objects)
            logging.info(f"Extracted {len(model_names)} model objects from the dataset.")
            # Pass to get_user_selection for interactive model selection
            selected_models = get_user_selection(model_names)
            return selected_models
        except Exception as e:
            logging.error(f"Error fetching model objects: {e}")
            return []
        finally:
            db.Close()

    elif models_option == 'models.csv':
        """
        example models.csv:
        model_name
        RPS_080_SPS_070
        RPS_000_SPS_000_toyForAlgebraic
        WindFarm_RegionA
        SolarFarm_RegionB
        CoalPlant_RegionC
        HydroPlant_RegionD
        """
        # Read models from models.csv file
        models_df = pd.read_csv(os.path.join(script_dir, 'models.csv'))
        return models_df['model_name'].tolist()

    else:
        # Assume models_option is a specific model name or a comma-separated list of names
        return models_option.split(',')

# Interactive model selection based on user input and optional filtering
def get_user_selection(model_names):
    """
    Get user selection from the list of model names.
    If the user provides a filter keyword, models are filtered by it.
    Allows selection by ranges and numbers for flexibility.
    """
    while True:
        filter_keyword = input("Enter a keyword to filter model objects (or press Enter to view all): ").strip()
        filtered_models = [name for name in model_names if filter_keyword.lower() in name.lower()] if filter_keyword else model_names

        if not filtered_models:
            print("No models found with the specified keyword. Please try again.")
            continue

        print("Available model objects:")
        for idx, name in enumerate(filtered_models, start=1):
            print(f"{idx}. {name}")

        selection = input("Enter the numbers of the models you want to submit (comma-separated, ranges allowed e.g., 10-20, 30, 40-45): ").strip()

        try:
            selected_indices = []
            for part in selection.split(","):
                if "-" in part:
                    start, end = map(int, part.split("-"))
                    selected_indices.extend(range(start, end + 1))
                else:
                    selected_indices.append(int(part.strip()))
            selected_models = [filtered_models[idx - 1] for idx in selected_indices]
            logging.info(f"User selected the following models: {selected_models}")
            return selected_models
        except (ValueError, IndexError) as e:
            logging.error(f"Invalid selection input: {e}")
            print("Invalid selection. Please try again.")

# CLI Helper: Retrieve the latest engine ID
def get_latest_engine_id():
    """Fetches the latest engine ID by release date from available PLEXOS engines."""
    try:
        command = ["pxc", "simulation", "engine", "list", "--format", "json"]
        result = run_cli_command(command)
        if result["success"]:
            engines = json.loads(result["output"])
            latest_engine = max(engines, key=lambda eng: datetime.fromisoformat(eng["ReleasedDate"].replace("Z", "+00:00")))
            logging.info(f"Selected latest engine ID: {latest_engine['Id']} ({latest_engine['Version']})")
            return latest_engine["Id"]
        else:
            logging.error("Failed to retrieve engine list.")
            return None
    except Exception as e:
        logging.error(f"Error fetching engine ID: {e}")
        return None

def get_vm_type():
    vm_setting = get_config_value('vm_type', '2-16')
    core, ram = map(int, vm_setting.split('-'))
    return {"cpuCores": core, "memoryInGb": ram}

# CLI Helper: Retrieve the latest changeset ID
def get_latest_changeset_id(study_id):
    """Fetches the latest changeset ID by update date for a given study."""
    try:
        command = ["pxc", "study", "changeset", "list", "--studyId", study_id, "--format", "json"]
        result = run_cli_command(command)
        if result["success"]:
            changesets = json.loads(result["output"])
            latest_changeset = max(changesets, key=lambda cs: datetime.fromisoformat(cs["UpdatedDate"].replace("Z", "+00:00")))
            logging.info(f"Selected latest changeset ID: {latest_changeset['Id']} (Updated: {latest_changeset['UpdatedDate']})")
            return latest_changeset["Id"]
        else:
            logging.error("Failed to retrieve changeset list.")
            return None
    except Exception as e:
        logging.error(f"Error fetching changeset ID: {e}")
        return None

# CLI Helper: Get machine recommendation with raw output logging
def get_machine_recommendation(study_id, model_name):
    """
    Retrieves machine recommendations based on the latest changeset.
    
    Args:
        study_id (str): The ID of the study.
        model_name (str): The name of the model for which to get a recommendation.
        
    Returns:
        dict: Recommended machine specs, or None if an error occurs.
    """
    changeset_id = get_latest_changeset_id(study_id)
    if not changeset_id:
        logging.error("Failed to retrieve latest changeset ID for machine recommendation.")
        return None
    
    try:
        command = [
            "pxc", "insights", "get-machine-recommendation",
            "--studyId", study_id,
            "--changesetId", changeset_id,
            "--modelName", model_name,
            "--format", "json"
        ]
        result = run_cli_command(command)
        if result["success"]:
            try:
                recommendation = json.loads(result["output"])
                logging.info(f"Machine recommendation retrieved: {recommendation}")
                return recommendation
            except json.JSONDecodeError:
                logging.error(f"Failed to parse machine recommendation output: {result['output']}")
                return None
        else:
            logging.error("Failed to retrieve machine recommendation.")
            return None
    except Exception as e:
        logging.error(f"Error fetching machine recommendation: {e}")
        return None

def submit_models_to_cloud(selected_models, study_id):
    """
    Submit selected models to PLEXOS Cloud for execution using the CLI.

    Args:
        selected_models (list): List of selected model names.
        study_id (str): Study ID for the cloud submission.
    """
    # Cloud VM types for fallback in ascending order
    vm_configurations = [
        {"cpuCores": 2, "memoryInGb": 16},
        {"cpuCores": 4, "memoryInGb": 32},
        {"cpuCores": 8, "memoryInGb": 64},
        {"cpuCores": 16, "memoryInGb": 128},
        {"cpuCores": 20, "memoryInGb": 160},
        {"cpuCores": 32, "memoryInGb": 256},
        {"cpuCores": 48, "memoryInGb": 384},
        {"cpuCores": 64, "memoryInGb": 512}
    ]
    
    try:
        for model in selected_models:
            # Get machine recommendation for the specific model
            machine_recommendation = get_machine_recommendation(study_id, model)
            if machine_recommendation:
                recommended_cpu = machine_recommendation.get("cpuCores", 2)
                recommended_memory = machine_recommendation.get("memoryInGb", 16)
                logging.info(f"Using recommended CPU: {recommended_cpu}, Memory: {recommended_memory} GB for model: {model}")
            else:
                logging.warning(f"No machine recommendation available for model {model}. Using smallest VM configuration as default.")
                recommended_cpu = vm_configurations[0]["cpuCores"]
                recommended_memory = vm_configurations[0]["memoryInGb"]

            # Get the latest engine ID for the simulation
            engine_id = get_latest_engine_id()
            if engine_id:
                # Try each VM configuration until a successful submission or all options are exhausted
                for config in vm_configurations:
                    cpu = config["cpuCores"]
                    memory = config["memoryInGb"]
                    
                    enqueue_command = [
                        "pxc", "simulation", "enqueue", "standard",
                        "--studyId", study_id,
                        "--models", model,
                        "--engineId", engine_id,
                        "--cpuCores", str(cpu),
                        "--memoryInGb", str(memory),
                        "--format", "json"
                    ]
                    enqueue_response = run_cli_command(enqueue_command)

                    if enqueue_response["success"]:
                        try:
                            enqueue_data = json.loads(enqueue_response["output"])
                            # Handle response as a list
                            if isinstance(enqueue_data, list) and len(enqueue_data) > 0:
                                simulation_id = enqueue_data[0].get("Id")
                                execution_id = enqueue_data[0].get("ExecutionId")
                                if simulation_id:
                                    logging.info(f"Successfully submitted model '{model}' with Simulation ID: {simulation_id}, Execution ID: {execution_id}")
                                    break  # Exit the fallback loop if submission is successful
                                else:
                                    logging.error(f"Failed to retrieve Simulation ID for model '{model}'.")
                            else:
                                logging.error(f"Unexpected response format: {enqueue_data}")
                        except json.JSONDecodeError:
                            logging.error(f"Failed to parse enqueue response for model '{model}'. Output: {enqueue_response['output']}")
                    else:
                        logging.error(f"Failed to enqueue model '{model}' with CPU: {cpu}, Memory: {memory} GB. Trying next VM configuration.")
                else:
                    logging.error(f"All configurations failed for model '{model}'. Exiting submission for this model.")
            else:
                logging.error("Unable to retrieve the latest engine ID. Exiting...")
    except Exception as e:
        logging.error(f"Error submitting models to cloud: {e}")

def fetch_local_xml_path(study_id):
    """
    Fetch the local XML path for a given study ID if it exists locally.

    Args:
        study_id (str): The study ID in PLEXOS Cloud.

    Returns:
        str or None: Path to the local XML if available, or None otherwise.
    """
    try:
        # Run `list-local` to check if the study ID is linked to a local XML
        command = ["pxc", "study", "list-local", "--format", "json"]
        result = run_cli_command(command)
        
        if result["success"]:
            local_studies = json.loads(result["output"])
            # Find the study with the matching study ID
            for study in local_studies:
                if study["StudyId"] == study_id:
                    logging.info(f"Found local XML path for study {study_id}: {study['StudyPath']}")
                    return study["StudyPath"]
        else:
            logging.warning("Failed to retrieve local study list.")
    except Exception as e:
        logging.error(f"Error fetching local XML path: {e}")
    
    return None

# Example main function 12,14-55,57-147,154-164,166-177
def main():
    # Fetch study ID and ensure XML path is available if needed
    study_id = get_study_id()
    plexos_xml_path = get_config_value('plexos_xml_path', default='')
    
    # If XML path is missing but study ID exists, attempt to fetch it locally
    if not plexos_xml_path and study_id:
        plexos_xml_path = fetch_local_xml_path(study_id)
        if not plexos_xml_path:
            logging.error("No local XML found for the provided study ID. Exiting.")
            sys.exit(1)

    # Retrieve the engine ID
    engine_id = get_latest_engine_id() if get_config_value('engine', 'latest') == 'latest' else get_config_value('engine')

    # Sync model to Cloud if XML path is available, otherwise use provided study ID
    try:
        study_id = sync_model_to_cloud(study_id, plexos_xml_path)
    except Exception as e:
        logging.error("Failed to sync the PLEXOS XML to the cloud. Exiting.")
        sys.exit(1)

    # Fetch models from XML and prompt user for selection or load from models.csv
    models = fetch_model_objects(plexos_xml_path)
    
    # Determine model selection method based on config
    model_selection_option = get_config_value('models', 'show models')
    if model_selection_option == 'show models':
        selected_models = get_user_selection(models)
    elif model_selection_option == 'use models.csv file':
        selected_models = pd.read_csv('models.csv')['model_name'].tolist()
    else:
        selected_models = [model_selection_option]  # Direct model name from config

    # Get VM specifications
    vm_specs = get_vm_type()

    # Enqueue each selected model for PLEXOS Cloud submission
    for model in selected_models:
        command = [
            "pxc", "simulation", "enqueue", "standard",
            "--studyId", study_id,
            "--models", model,
            "--engineId", engine_id,
            "--cpuCores", str(vm_specs['cpuCores']),
            "--memoryInGb", str(vm_specs['memoryInGb']),
            "--format", "json"
        ]
        response = run_cli_command(command)
        if response['success']:
            logging.info(f"Submitted model {model}")
        else:
            logging.error(f"Failed to submit model {model}: {response['error']}")

if __name__ == "__main__":
    main()
