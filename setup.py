#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

dependencies = []
links = []

setup(
    name='py-infusionsoft',
    version='0.2',
    description='python wrapper for InfusionSoft API',
    author='',
    author_email='',
    scripts=[],
    url='https://github.com/infusionsoft/Official-API-Python-Library',
    packages=find_packages(),
    include_package_data=True,
    install_requires=dependencies,
    dependency_links=links,
)
