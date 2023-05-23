""" creating a template file to design the project skeleton """
import os
import logging
from pathlib import Path
from dotenv import load_dotenv


logging.basicConfig(
    level= logging.INFO,
    format= "[%(asctime)s: %(levelname)s: %(lineno)s: %(module)s]: %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S",
    filemode= "a"
)

load_dotenv()
# project environment variables:
PROJECT_NAME = os.getenv("PROJECT_NAME")
REPO_NAME = os.getenv("REPO_NAME")
GITHUB_USER_NAME = os.getenv("GITHUB_USER_NAME")
AUTHOR_NAME = os.getenv("AUTHOR_NAME")
AUTHOR_EMAIL = os.getenv("AUTHOR_EMAIL")
PACKAGE_NAME = os.getenv("PACKAGE_NAME")
COMMAND_NAME = os.getenv("COMMAND_NAME")
LICENCE_NAME = os.getenv("LICENCE_NAME")
PYTHON_VERSION = os.getenv("PYTHON_VERSION")
YEAR = os.getenv("YEAR")

env_vars = [PROJECT_NAME, REPO_NAME, GITHUB_USER_NAME, AUTHOR_NAME, AUTHOR_EMAIL,
                               PACKAGE_NAME, COMMAND_NAME, LICENCE_NAME, PYTHON_VERSION, YEAR]
if not all(env_vars):
    raise ValueError("one or more missing variables from env_vars")

logging.info("creating project by name: %s", PROJECT_NAME)

# list of files and directories:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/cli.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "requirements.txt",
    "init_setup.sh",
    "pyproject.toml",
    "tox.ini",
    "mkdocs.yaml",
    "docker-compose.yaml",
    "Makefile",
    "setup.py",
    "setup.cfg",
]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info("creating directory at: %s for file name: %s", filedir, filename)
    if not os.path.exists(filepath) or os.path.getsize(filepath)==0:
        with open(filepath, 'w', encoding= "utf-8") as f:
            pass
        logging.info(" creating new file: %s at file path: %s", filename, filepath)
    else:
        logging.info("file already present at: %s", filepath)

class UpdateContent:
    """ this class is used to update the content """
    def __init__(self, path:str, **kwargs):
        self.path = path
        self.kwargs= kwargs
        self.content = None
    def read_content(self):
        """ this method is used to read the content"""
        with open(self.path, 'r', encoding= "utf-8") as file:
            self.content = file.read()
        if self.content !="":
            logging.info("content is read successfully from path: %s", self.path)
    def replace_content(self):
        """ this method is used to replace/update the content """
        if self.content != "":
            for key, value in self.kwargs.items():
                self.content= self.content.replace(f"<{key}>", value)
    def write_content(self):
        """ this method is used to write the content """
        if self.content != "":
            with open(self.path, 'w', encoding="utf-8") as file:
                file.write(self.content)
            logging.info("content is written & updated successfully to path: %s", self.path)
path_and_kwargs = {
    "pyproject.toml": {
        "REPO_NAME": REPO_NAME,
        "GITHUB_USER_NAME": GITHUB_USER_NAME,
        "PACKAGE_NAME": PACKAGE_NAME,
        "AUTHOR_EMAIL": AUTHOR_EMAIL,
        "COMMAND_NAME": COMMAND_NAME,
        "LICENCSE_NAME": LICENCE_NAME
    },
    "mkdocs.yaml": {
        "PACKAGE_NAME": PACKAGE_NAME,
        "GITHUB_USER_NAME": GITHUB_USER_NAME,
        "YEAR": YEAR,
        "REPO_NAME": REPO_NAME,
        "AUTHOR_NAME": AUTHOR_NAME
    },
    "init_setup.sh": {
        "PYTHON_VERSION": PYTHON_VERSION,
    },
    "docker-compose.yaml": {
        "PROJECT_NAME": PROJECT_NAME
    }
}

for path, kwargs in path_and_kwargs.items():
    update_content= UpdateContent(path= Path(path), **kwargs)
    update_content.read_content()
    update_content.replace_content()
    update_content.write_content()
    