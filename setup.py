#!/usr/bin/env python

from distutils.core import setup
from pyavrophonetic import __version__

setup(name='pybengengphonetic',
      version=__version__,
      description='Python implementation to convert bengali to phonetic',
      long_description=open('README.rst', 'rt').read(),
      author='Subrata Sarkar',
      author_email='subrotosarkar32@gmail.com',
      url='https://github.com/SubrataSarkar32/pyAvroPhonetic/',
      packages=['pybengenghonetic',],
      install_requires=["simplejson >= 3.0.0",'pyttsx >=1.1],
      license='GNU GPL v3 or later',
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ]
      )
