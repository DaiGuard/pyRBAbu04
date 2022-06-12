from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pyRBAbu04',
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DaiGuard/pyRBAbu04',
    author='DaiGuard',
    author_email='daiguard0224@gmail.com',
    license='MIT',
    packages=find_packages(),    
    install_requires=_requires_from_file('requirements.txt'),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]    
    python_requires='>=3.9',
)