# Import necessary modules
import os
from pathlib import Path

# Define the name of the package
package_name = "DimondPricePrediction"

# List of files to be created
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    # "init_setup.sh",
]

# Loop through each file path in the list
for filepath in list_of_files:
    # Convert the file path to a Path object
    filepath = Path(filepath)
    
    # Split the file path into directory and filename
    filedir, filename = os.path.split(filepath)
    
    """ 
    Check if the directory exists. 
    If not, create the directory using os.makedirs with exist_ok=True 
    (won't raise an error if the directory already exists).
    """
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    # Check if the file doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode, creating it if necessary, and do nothing (empty file)
        with open(filepath, "w") as f:
            pass
    else:
        # Print a message if the file already exists
        print("file already exists")
