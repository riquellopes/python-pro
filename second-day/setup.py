#!/usr/bin/env python

from setuptools import setup

setup(
    name="RiquellopesAvatar",
    version="1.0",
    description="Simple get avatar from github.",
    author="Henrique Lopes",
    author_email="contato@henriquelopes.com.br",
    packages=["avatar"],
    install_requires=[
        "requests == 2.10.0"
    ])
