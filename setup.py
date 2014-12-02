#! /usr/bin/env python

from setuptools import setup

long_description = """
This is a package for organizing and testing various python practice algorithms.
"""

setup(
    name="python-practice",
    version="0.1-dev",
    description="python practice modules",
    long_description=long_description,
    # The project URL.
    url='http://github.com/jwhite007/python-practice',
    # Author details
    author='James T. White',
    author_email='jwhite007@comcast.net',
    # Choose your license
    #   and remember to include the license text in a 'docs' directory.
    # license='MIT',
    packages=['practice_modules', 'practice_modules_tests'],
    # also: find_packages(exclude=['tests',])
    install_requires=['setuptools', ]
    # also test_requires=[]
)
