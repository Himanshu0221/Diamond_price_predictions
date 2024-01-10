
from setuptools import find_packages, setup
from typing import List

# a variable representing '-e .' as a constant
# HYPEN_E_DOT = '-e .'

# # Function to read requirements from a file and return them as a list

# def get_requirements(file_path: str) -> List[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]

#         # Unused code: Remove '-e .' from requirements if present
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements

# Set up the package using the setup function from setuptools
setup(
    name='DimondPricePrediction',  # Package name
    version='0.0.1',  # Package version
    author='himanshu tagare',  # Author's name
    author_email='himanshu_tagare@yahoo.in',  # Author's email
    install_requires=["scikit-learn","pandas","numpy"],  # List of dependencies
    packages=find_packages()  # Automatically discover and include all packages in the distribution
)
