from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .' # This is the string which is to be removed from the requirements file
def get_requirements(filepath:str) -> List[str]:  #filepath is the path of the requirements file and it returns a -> List type data
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:    #opening the requirements file
        requirements=file_obj.readlines()   #reading the file
        requirements = [req.replace('\n','') for req in requirements]   # While reading the nest line will be considered as '/n' and so replace it with ''

        if HYPHEN_E_DOT in requirements:   #If the line contains '-e.' then remove it
            requirements.remove(HYPHEN_E_DOT)

    return requirements

#These are the parameters of the package
setup(
name = 'ML project',
version='0.01',
author='mrinmoy',
author_email='mrinmoy.low2002@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)