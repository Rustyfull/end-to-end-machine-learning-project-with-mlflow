import os
from pathlib import  Path
import  logging


logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")

project_name = "mlproject"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html",
    "pyproject.toml"


]



def create_structure():
    for path in list_of_file:
        path = Path(path)
        file_dir, file_name = os.path.split(path)

        if file_dir != "":
            os.makedirs(file_dir,exist_ok=True)
            logging.info(f"Creating directory: {file_dir} for the file: {file_name}")


        if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
            with open(path,"w") as f:
                pass
            logging.info(f"Creating empty file: {path}")

        else:
            logging.info(f"{file_name} is already exist")


if __name__ == "__main__":
    create_structure()