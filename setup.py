from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .' # this string may be fine in the requirement.txt file
def get_requirements(file_path:str)->List[str]:
    ''' This function will return the list of requirements'''
    requirements=[]
    #starting for loop
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #while reading requirement from requirement.txt next line \n will be captuchered to remove it 
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements # end of for loop
setup(
    name='mlproject',
    version='0.0.1',
    author='Nikhil',
    author_email='nikhil.dinnu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )