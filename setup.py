#!/usr/bin/env python

from distutils.core import setup

setup(name='MDorder',
      version='0.1',
      description='Compute Amide bond S2 order parameters from MD trajectories',
      author='Oliver Schillinger',
      author_email='oliver@schillinger-ttp.de',
      url='https://github.com/schilli/MDorder',
      packages=['MDorder'],
      package_data={'MDorder': ['test/*']}
     )
