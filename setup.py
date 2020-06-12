#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 8, 0):
    raise Exception("This project designed for Python >= 3.8.")

setup(
    name="transnb",
    # version="0.0.1",
    description="Twitter bot with solidarity and love for trans and non-binary people",
    author="Andy Herd",
    author_email="40397581+herdingdata@users.noreply.github.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        transnb-tweet=transnb.commands:tweet
        transnb-all=transnb.commands:all_messages
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
