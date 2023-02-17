#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Daniel Cruz",
    author_email='danielcruz.alu.lmb@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Script that scrapes data in a website called coinranking",
    entry_points={
        'console_scripts': [
            'cryptos_webscrapping=cryptos_webscrapping.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cryptos_webscrapping',
    name='cryptos_webscrapping',
    packages=find_packages(include=['cryptos_webscrapping', 'cryptos_webscrapping.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DanielCruzDataEngineer/cryptos_webscrapping',
    version='1',
    zip_safe=False,
)
