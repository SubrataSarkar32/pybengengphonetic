#!/usr/bin/env python

"""Python implementation of Avro Phonetic in hindi.

-------------------------------------------------------------------------------
Copyright (C) 2016 Subrata Sarkar <subrotosarkar32@gmail.com>
modified by:- Subrata Sarkar <subrotosarkar32@gmail.com>
original by:- Kaustav Das Modak <kaustav.dasmodak@yahoo.co.in.
Copyright (C) 2013 Kaustav Das Modak <kaustav.dasmodak@yahoo.co.in.

This file is part of pyAvroPhonetic.

pyAvroPhonetic is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyAvroPhonetic is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyAvroPhonetic.  If not, see <http://www.gnu.org/licenses/>.

"""

def utf(text):
    """Shortcut funnction for encoding given text with utf-8"""
    try:
        output = unicode(text, encoding='utf-8')
    except UnicodeDecodeError:
        output = text
    except TypeError:
        output = text
    return output
