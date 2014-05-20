#! /usr/bin/env python

from setuptools import setup

setup(name="lsystem",
      version="0.1",
      author="Rory McCann",
      author_email="rory@technomancy.org",
      packages=['lsystem'],
      license = 'GPLv3+',
      test_suite='lsystem.tests',
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
      ],
)
