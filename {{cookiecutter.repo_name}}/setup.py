#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

from setuptools import setup, find_packages

INSTALL_REQUIRES = ['attrdict']

DEV_REQUIRES = ['bumpversion', 'pytest', 'pytest-cov', 'pre-commit', 'prospector', 'yapf']

PACKAGE_INFO = {
    'name': '{{ cookiecutter.repo_name }}',
    'version': '0.0.0',
    'description': '{{ cookiecutter.project_short_description }}',
    'email': '{{ cookiecutter.email }}',
    'author': '{{ cookiecutter.full_name }}',
    'url': '{{ cookiecutter.repo_url }}',
    'python_requires': '>=3.6',
    'install_requires': INSTALL_REQUIRES,
    'extras_require': {
        'dev': DEV_REQUIRES
    },
    'license': '{{ cookiecutter.open_source_license }}',
    'packages': find_packages('src', exclude=['tests']),
    'package_dir': {
        '': 'src'
    },
}

setup(**PACKAGE_INFO)
