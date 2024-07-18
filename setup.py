#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, os


# helper
helper = "helper{sep}*.*".format(sep=os.sep)

setup(
    name='dProgBb',
    version='1.2',
    description='Detect Program Bug Bounty',
    author='pikpikcu&Hasim',
    author_email='N/A',
    url='https://github.com/xcapri/dProgBb',
    packages=find_packages(),
    package_data={'core': [helper]},
    include_package_data=True,
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'dprog=core.main:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
    ],
)
