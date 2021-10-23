#!/usr/bin/env python

try:
    from setuptools import setup

    from pybengengphonetic import __version__

    setup(name='pybengengphonetic',
          version='1.0.1',
          description='Python implementation to convert bengali to phonetic',
          long_description=open('README.rst', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://bitbucket.org/SubrataSarkar32/pybengengphonetic/',
          packages=['pybengengphonetic','pybengengphonetic.utils'],
          package_data = {'pyhinavrophonetic': ['*.rst', 'resources/*.json','utils/resources/*.json']},
          include_package_data = True,
          install_requires=["simplejson >= 3.0.0",'pyttsx3 >=2.90'],
          license='GNU GPL v3 or later',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            ]
          )

except ImportError:
    print('Install setuptools')
