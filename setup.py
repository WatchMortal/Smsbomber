#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()

setup(
    name='PyPhisher',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MythDeath',
    author_email='"X"',
    license="MIT",
    url='https://github.com/MythDeath/PyPhisher/',
    scripts=['pyphisher'],
    install_requires=["requests", "bs4", "rich"]
)
