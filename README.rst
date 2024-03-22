==============
pybengengphonetic
==============
Python implementation to convert unicode bengali text to speable english text for pyttsx and to english phonetic


License
=======

Copyright (C) 2016 Subrata Sarkar <subrtosarkar32@gmail.com>.

::

    This file is part of pybengengphonetic.

    pybengengphonetic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pybengengphonetic is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pybengengphonetic. If not, see <http://www.gnu.org/licenses/>.

The full license text can be found in ``LICENSE``.

Usage
=====

::

    from pybengengphonetic import conparse
    conparse.convert_to_pyttsx_speakable(u'\u0995\u09c7\u09ae\u09a8 \u0986\u099b')
    conparse.speak(u'\u0995\u09c7\u09ae\u09a8 \u0986\u099b')

Installation
============

Using Git:

::

    $ git clone https://github.com/SubrataSarkar32/pybengengphonetic.git
    $ cd pybengengphonetic
    $ sudo python setup.py install


Using Pip:

::

    $ sudo pip install pybengengphonetic

Contributing
============

**Fork** -> **Do your changes** -> **Send a Pull Request**. It's that
easy!

Coding style follows `PEP 8`_ along with `PEP 257`_ for Docstring
conventions.

Also, if you find any bugs, please report them in the Issues queue. As
always, before you report any new issue, please check that it has not
been already posted by someone else.

This library has been derived from pyAvroPhonetic [https://github.com/kaustavdm/pyAvroPhonetic]
