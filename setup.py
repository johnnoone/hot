#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils import sysconfig
site_packages_path = sysconfig.get_python_lib()

setup(
    name='hot',
    data_files=[
        (site_packages_path, ["zyx-hot.pth"])
    ],
    packages=find_packages()
)
