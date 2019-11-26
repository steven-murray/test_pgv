#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import find_packages, setup

def myversion():
    from setuptools_scm.version import guess_next_dev_version

    def branch_scheme(version):
        return guess_next_dev_version(version) if version.exact else guess_next_dev_version(version)+"b{}".format(version.branch)

    return {'local_scheme': branch_scheme, "version_scheme": branch_scheme}

setup(
    name="test_pgv",
    packages=find_packages(),
    python_requires=">=3.5",
    use_scm_version=myversion,
    setup_requires=['setuptools_scm']
)
