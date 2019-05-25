#!/usr/bin/env python

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, convert_path
    #FIXME: check the base_path in the setup().packages
    def find_packages(base_path):
        base_path = convert_path(base_path)
        found = []
        for root, dirs, files in os.walk(base_path, followlinks=True):
            dirs[:] = [d for d in dirs if d[0] != '.' and d not in ('ez_setup', '__pycache__')]
            relpath = os.path.relpath(root, base_path)
            parent = relpath.replace(os.sep, '.').lstrip('.')
            if relpath != '.' and parent not in found:
                continue
            for dir in dirs:
                if os.path.isfile(os.path.join(root, dir, '__init__.py')):
                    package = '.'.join((parent, dir)) if parent else dir
                    found.append(package)
        return found

import crypot

# TODO: prepare in doc about the 'requirements.txt'
install_requires = [
    'gmpy2',
    'pycrypto',
    'pwntools',
]

setup(
    name = "crypot",
    #version  =  "0.0,1",
    version = crypot.__version__,
    author = "teambi0s",
    author_email = "sayoojsamuelgreat@gmail.com",
    license=crypot.__license__,
    url = "https://github.com/sayoojsamuel/crypot",
    description = "Library of common crypto exploits",
    long_description=crypot.__doc__,
    extras_require={
        ':python_version < "3.0"': [
            'future'
        ]
    },
    #FIXME: check for f() args in import section
    packages = find_packages(),
    classifiers =  ['Development Status :: Alpha',
                    'Intended Audience :: Science/Research/CTFers',
                    'Natural Language :: English',
                    'Operating System :: Linux preferably',
                    'Programming Language :: Python :: 2',
                    'License :: MIT License',
                    'Topic :: Scientific/Engineering :: Mathematics',
                    'Topic :: Security :: Cryptography',
                    ],
)

