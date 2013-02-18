import os
import re
from setuptools import setup, find_packages

rel_file = lambda *args: os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)

def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()

def get_long_description():
    return read_from(rel_file('README.md'))

def get_version():
    data = read_from(rel_file('remotemodels', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", data).group(1)

setup(
    name='remotemodels',
    description='Declarative dictionary-based model classes for Python',
    long_description=get_long_description(),
    version=get_version(),
    packages=find_packages(),
    url='https://github.com/tzangms/remotemodels/',
    author='Ming Hsien Tzang',
    author_email='tzangms@gmail.com',
    license='Public Domain',
    install_requires=["python-dateutil==1.5", "PySO8601"],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
