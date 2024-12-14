from setuptools import setup,find_packages
from typing import List

Hypen_dot_e='-e .'
def get_requirements(filepth:str)->[List]:
    requirements=[]
    with open(filepth) as f:
        requirements=f.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)

    return requirements

setup(
    name='Traffic-Sign-Detector-Yolov5',
    version='1.0',
    author='Arpanchakraborty23',
    author_email='arpanchakaborty500@gmail.com',
    url='https:\\github.com/arpanchakraborty23/Traffic-Sign-Detector-Yolov5.git',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
)