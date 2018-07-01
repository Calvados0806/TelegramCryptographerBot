"module which contains some crypto functions"
from hashlib import sha256
from itertools import cycle

class Shift(object):
    def __init__(self, char=''):
        self._char = char
        self._ascii = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z'
        ]
        self._cyrillic = [
            'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и',
            'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я'
        ]

    def shift(self, count):
        isCyrillic = self.is_cyrillic()
        isLower = self._char.lower() == self._char
        if isCyrillic:
            container = self._cyrillic
            isInContainer = self._char.lower() in container
            mod = 33
        else:
            container = self._ascii
            isInContainer = self._char.lower() in container
            mod = 26
        if not isInContainer:
            return self._char
        elif isLower:
            ind = container.index(self._char)
            return container[(ind + count) % mod]
        else:
            ind = container.index(self._char.lower())
            return container[(ind + count) % mod].upper()

    def change_char(self, new_char):
        self._char = new_char

    def is_cyrillic(self):
        return ord(self._char) >= 1040

    def is_symbol(self):
        return self._char.lower() in self._cyrillic or self._char.lower() in self._ascii

    def sid(self):
        try:
            sid = self._cyrillic.index(self._char.lower())
            return sid
        except ValueError:
            try:
                sid = self._ascii.index(self._char.lower())
                return sid
            except ValueError:
                return 0

def caesar(text, key, decode=False):
    "encode or decode message using caesar cipher"
    final = ""
    symb = Shift()
    for symbol in text:
        symb.change_char(symbol)
        if not decode:
            final += symb.shift(key)
        else:
            final += symb.shift(-key)
    return final

def vigenere(text, key, decode=False):
    "encode or decode text using vigenere cipher"
    final = ""
    cycle_key = ""
    symb1 = Shift()
    symb2 = Shift()
    key_iter = cycle(key)

    for s in text:
        symb1.change_char(s)
        if symb1.is_symbol():
            cycle_key += next(key_iter).lower()
        else:
            cycle_key += s

    for stext, skey in zip(text, cycle_key):
        symb2.change_char(stext)
        symb1.change_char(skey)
        if not decode:
            final += symb2.shift(symb1.sid())
        else:
            final += symb2.shift(-symb1.sid())
    return final

def hash_(text):
    "hash some text using standard sha256"
    result = sha256(bytes(text, encoding='utf-8'))
    return result.hexdigest()
