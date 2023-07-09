from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements: requirements.remove("-e .")
        return requirements

setup(
    name="DiamondPricePred",
    version="1.0.0",
    author="Gowtham",
    author_email="gowthham.nambiaarorar@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()

)