#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.develop import develop as _develop
from setuptools.command.install import install as _install
from distutils import sysconfig
from distutils.sysconfig import get_python_lib
import sys


# In case of .pth-fu technics
class MyDevelop(_develop):
    pass


# Fixes python setup.py install
class MyInstall(_install):

    def initialize_options(self):
        super().initialize_options()
        # avoid to install as an .egg
        self.old_and_unmanageable = True


# switch between import strategies
pths = []
if sys.version_info >= (3, 4, 0):
    pths.append('zyx-hot-py3.4.pth')
elif sys.version_info >= (3, 0, 0):
    pths.append('zyx-hot-py3.0.pth')
elif sys.version_info >= (2, 7, 0):
    pths.append('zyx-hot-py2.7.pth')
else:
    raise RuntimeError("Python >= 2.7 only")


setup(
    name='hot',
    data_files=[
        (get_python_lib(prefix=''), pths)
    ],
    packages=find_packages(),
    zip_safe=False,
    cmdclass={
        'install': MyInstall,
        'develop': MyDevelop
    }
)

"""

.. Notes::

    get_python_lib(prefix='') : ensure it is relative
    http://blog.dscpl.com.au/2015/04/automatic-patching-of-python.html


"""
