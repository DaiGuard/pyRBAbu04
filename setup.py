from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pyRBAbu04',
    version='0.0.1',
    description='',
    url='https://github.com/DaiGuard/pyRBAbu04',
    author='DaiGuard',
    author_email='daiguard0224@gmail.com',
    license='MIT',
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=_requires_from_file('requirements.txt'),    
)