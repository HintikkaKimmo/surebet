#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Kimmo Hintikka",
    author_email='hintikkakimmo@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="surebet is Python sport betting library allowing you to easily convert "
                "betting odds, calculate returns, calculate arbitrage betting opportunities and more",
    entry_points={
        'console_scripts': [
            'surebet=surebet.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT License",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='surebet',
    name='surebet',
    packages=find_packages(include=['surebet']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/HintikkaKimmo/surebet',
    version='0.1.1',
    zip_safe=False,
)
