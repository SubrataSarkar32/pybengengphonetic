#!/usr/bin/env python

try:
    from setuptools import setup, find_packages

    from pybengengphonetic import __version__

    setup(name='pybengengphonetic',
          version=__version__,
          description='Python implementation to convert bengali to phonetic',
          long_description=open('README.rst', 'rt').read(),
          long_description_content_type='text/markdown',
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://github.com/SubrataSarkar32/pybengengphonetic',
          packages=find_packages(),
          package_data = {'pybengengphonetic': ['*.rst', 'resources/*.json']},
          include_package_data = True,
          install_requires=['pyttsx3 >=2.90'],
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
