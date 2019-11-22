#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
from os.path import dirname, join

from setuptools import find_packages, setup

import pygitversion
pygitversion.write_git_info_file(join(dirname(__file__), 'test_pgv'))

def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()

setup(
    name="test_pgv",
    version="0.1.0",
    license="MIT",
    description="Test-repo for pygitversion",
    author="Radio Astronomy Software Group",
    author_email="steven.g.murray@asu.edu",
    url="https://github.com/steven-murray/test_pgv",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    python_requires=">=3.5",
    install_requires=['pygitversion'],
)
