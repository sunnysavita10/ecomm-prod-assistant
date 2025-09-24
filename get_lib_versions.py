import importlib.metadata
from pathlib import Path

file_path = Path.cwd()/ "requirements.txt"


def get_requirements(file_path:str)->list[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.split('==')[0] if "==" in req else req.replace('\n', '') for req in requirements]
    return requirements

packages = get_requirements(file_path)

for package in packages:
    try:
        version = importlib.metadata.version(package)
        print(f"{package}== {version}")
    except importlib.metadata.PackageNotFoundError:
        version = "not installed"
        print(f"{package} ({version})")