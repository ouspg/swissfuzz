#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "swissfuzz",
    version = "0.4",
    author = "Pekka Pietikäinen",
    author_email = "pp@ee.oulu.fi",
    description = ("A framework for robustness testing of arbitrary networked protocols"),
    license = "BSD",
    keywords = "fuzzing networking radamsa",
    url = "https://code.google.com/p/ouspg/",
    packages=['swissfuzz'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Testing",
    ],

    extras_require= {'SCTP': ['pysctp>=0.6']},
    dependency_links = ['https://github.com/philpraxis/pysctp/tarball/master#egg=0.6']
)
