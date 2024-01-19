import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "lesion_detection"  # Use snake_case for variable names

file_paths = [  # More descriptive name
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for file_path in file_paths:
    path_obj = Path(file_path)  
    directory_path, file_name = os.path.split(path_obj) 
    if directory_path != "":
        os.makedirs(directory_path, exist_ok=True)
        logging.info(f"Creating directory: {directory_path} for the file {file_name}")
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(path_obj, "w") as file:
            logging.info(f"Creating empty file: {file_name}")
    else:
        logging.info(f"{file_name} is already created")
