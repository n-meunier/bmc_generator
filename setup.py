#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# =============================================================================
#            Nicolas Meunier
# =============================================================================
# PROJECT : BMC Generator
# FILE : setup.py
# DESCRIPTION :
"""
Setup script that creates a package.

How to use it : python setup.py
Requirements:

========= ============== ======================================================
Version   Date           Comment
========= ============== ======================================================
0.1.0     2018/09/28     Initial version
========= ============== ======================================================
"""

# [IMPORTS]--------------------------------------------------------------------
from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
import os

# [MODULE INFO]----------------------------------------------------------------
__author__ = 'nmeunier'
__date__ = '2018/09/28'
__version__ = '0.1.0'
__url__ = 'https://github.com/n-meunier/bmc_generator'

# [GLOBAL & CONSTANT VARIABLES]------------------------------------------------
PACKAGE_NAME = 'bmc_generator'
DESCRIPTION = 'Funny sentence generator'
PLATFORMS = ['Linux']

# [CLASS DEFINITION]-----------------------------------------------------------
# install_reqs = parse_requirements('requirements.txt', session='hack')
# reqs = [str(ir.req) for ir in install_reqs]
setup(
    name=PACKAGE_NAME,
    description=DESCRIPTION,
    long_description=open(os.path.dirname(os.path.realpath(__file__)) +
                          '/README.md').read(),
    version=__version__,
    author=__author__,
    url=__url__,
    platforms=PLATFORMS,
    packages=find_packages(),
    include_package_data=True
    #install_requires=reqs,
    )
