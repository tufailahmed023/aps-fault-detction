from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirments.txt"
HYPEN_E_DOT = "-e ."
def get_requirements() ->List[str]:
    with open (REQUIREMENT_FILE_NAME) as reqirement_file:
        reqirement_list = reqirement_file.readlines()
    reqirement_list = [reqirement_name.replace("\n","") for reqirment_name in reqirement_list]

    if HYPEN_E_DOT in reqirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.1",
    author="tufail",
    author_email="tufailahmed023@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)