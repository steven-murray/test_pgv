#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import find_packages, setup

def myversion():
    from setuptools_scm.version import guess_next_dev_version

    def branch_scheme(version):
        if version.exact or version.node is None:
            return version.format_choice(
                "", "+d{time:{time_format}}", time_format="%Y%m%d"
            )
        else:
            if version.branch == "master":
                return version.format_choice(
                    "+{node}", "+{node}.d{time:{time_format}}", time_format="%Y%m%d"
                )
            else:
                return version.format_choice(
                    "+{node}[{branch}]", "+{node}[{branch}].d{time:{time_format}}", time_format="%Y%m%d"
                )
    return {'local_scheme': branch_scheme}

setup(
    name="test_pgv",
    packages=find_packages(),
    python_requires=">=3.5",
    use_scm_version=myversion,
    setup_requires=['setuptools_scm']
)
