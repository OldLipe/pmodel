#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys

from setuptools import find_packages, setup, Command

NAME = 'pmodel'
DESCRIPTION = 'Método de geração de séries temporais multifractais'
URL = 'https://github.com/oldlipe/pmodel'
EMAIL = 'lipecaso@gmail.com'
AUTHOR = 'Felipe Carvalho'
REQUIRES_PYTHON = '>=3.5.3'
VERSION = '0.0.1'

REQUIRED = [
    'numpy==1.14.5'
    ]

here = os.path.abspath(os.path.dirname(__file__))


try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['pmodel'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)