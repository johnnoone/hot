#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils import sysconfig
from distutils.sysconfig import get_python_lib

setup(
    name='hot',
    data_files=[
        (get_python_lib(prefix=''), ["zyx-hot.pth"])
    ],
    packages=find_packages(),
    zip_safe=False
)

"""

.. Notes::

    get_python_lib(prefix='') : ensure it is relative
    http://blog.dscpl.com.au/2015/04/automatic-patching-of-python.html


"""
