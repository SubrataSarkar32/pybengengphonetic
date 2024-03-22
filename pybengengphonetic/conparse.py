'''Python implementation of Avro Phonetic in bengali.

-------------------------------------------------------------------------------
Copyright (C) 2016 Subrata Sarkar <subrotosarkar32@gmail.com>
original by:- Subrata Sarkar <subrotosarkar32@gmail.com>

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
along with pybengengphonetic.  If not, see <http://www.gnu.org/licenses/>.

This tool converts unicode data to speakable pyttsx data
   using convert_to_pyttsx_speakable() and converts unicode data to speakable
   phonetic using convert_to_speakable_phonetic() and speak bengali
   using speak()
Example:convert_to_pyttsx_speakable(u'\\u0995\\u09c7\\u09ae\\u09a8 \\u0986\\u099b')
        speak(u'\\u0995\\u09c7\\u09ae\\u09a8 \\u0986\\u099b')'''

import string
from pybengengphonetic import hinavro


def convert_to_pyttsx_speakable(gitre=''):
    text2 = ''
    list19 = []
    for letter in gitre:
        list19 += [letter]
    singlet = 0
    while singlet < (len(list19)):
        try:
            str(list19[singlet])
            text2 += list19[singlet]
        except UnicodeEncodeError:
            matra = '\u09be\u09bf\u09c0\u09c1\u09c2\u09c3\u09c7\u09c8\u09cb\u09cc\u0985\u0986\u0987\u0988\u0989\u098a\u098b\u098c\u098f\u0990\u0993\u0994'
            try:
                if list19[singlet+1] in matra:
                    text2 += list19[singlet]
                    singlet += 1
                    text2 += list19[singlet]
                elif list19[singlet] in str(string.printable):
                    text2 = text2+list19[singlet]
                elif list19[singlet] in matra:
                    text2 = text2+list19[singlet]
                else:
                    text2 = text2+list19[singlet]+'o'
            except Exception:
                if list19[singlet] in str(string.printable):
                    text2 = text2+list19[singlet]
                elif list19[singlet] in matra:
                    text2 = text2+list19[singlet]
                else:
                    text2 = text2+list19[singlet]+'o'
        singlet += 1
    gitre = text2
    gitre = hinavro.parse(gitre)
    return gitre


def convert_to_speakable_phonetic(gitre=''):
    text2 = ''

    list19 = []

    for letter in gitre:
        list19 += [letter]
    singlet = 0
    while singlet < (len(list19)):
        try:
            str(list19[singlet])
            text2 += list19[singlet]
        except UnicodeEncodeError:
            matra = '\u09be\u09bf\u09c0\u09c1\u09c2\u09c3\u09c7\u09c8\u09cb\u09cc\u0985\u0986\u0987\u0988\u0989\u098a\u098b\u098c\u098f\u0990\u0993\u0994'
            try:
                if list19[singlet+1] in matra:
                    text2 += list19[singlet]
                    singlet += 1
                    text2 += list19[singlet]
                elif list19[singlet] in str(string.printable):
                    text2 = text2+list19[singlet]
                elif list19[singlet] in matra:
                    text2 = text2+list19[singlet]
                else:
                    text2 = text2+list19[singlet]+'o'
            except Exception:
                if list19[singlet] in str(string.printable):
                    text2 = text2+list19[singlet]
                elif list19[singlet] in matra:
                    text2 = text2+list19[singlet]
                else:
                    text2 = text2+list19[singlet]+'o'
        singlet += 1
    return text2


def speak(text=''):
    import pyttsx3 as pyttsx
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-60)    
    speakman1 = convert_to_pyttsx_speakable(gitre=text)
    engine.say(speakman1)
    engine.runAndWait()
    return 'Speak Over'


if __name__ == "__main__":
    speak('\u0995\u09c7\u09ae\u09a8 \u0986\u099b')
