"module which contains some crypto functions"
from hashlib import sha256

class Shift(object):
    def __init__(self, char):
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

def caesar(text, key, decode=False, ascii_=True):
    "encode or decode message using caesar cipher"
    if (ascii_):
        shift_lower = 97
        shift_upper = 65
        symb_count = 26
    else:
        shift_lower = 1072
        shift_upper = 1040
        symb_count = 40

    final = ""
    for symbol in text:
        if not decode:
            if symbol.islower():
                final += chr((ord(symbol) - shift_lower + key + symb_count) % symb_count + shift_lower)
            elif symbol.isupper():
                final += chr((ord(symbol) - shift_upper + key + symb_count) % symb_count + shift_upper)
            else:
                final += symbol
        else:
            if symbol.islower():
                final += chr((ord(symbol) - shift_lower - key + symb_count) % symb_count + shift_lower)
            elif symbol.isupper():
                final += chr(((ord(symbol) - shift_upper - key + symb_count) % symb_count) + shift_upper)
            else:
                final += symbol
    return final

def vigenere(text, key, decode=False, ascii_=True):
    "encode or decode text using vigenere cipher"
    final = ""
    new_key = ''
    i, j = 0, 0

    if (ascii_):
        shift_lower = 97
        shift_upper = 65
        symb_count = 26
    else:
        shift_lower = 1072
        shift_upper = 1040
        symb_count = 40

    while i < len(text):
        while j < len(key):
            if (i < len(text) and j < len(key) and (text[i] == ' ' or text[i] == ',' or text[i] == '!')):
                new_key += text[i]
                i += 1
            elif (i < len(text) and j < len(key) and (text[i] != ' ' or text[i] != ',' or text[i] != '!')):
                new_key += key[j]
                i += 1
                j += 1
            else:
                break
        j = 0

    for index, symbol in enumerate(text):
        if not decode:
            if symbol.islower():
                final += chr((ord(symbol) - shift_lower + (ord(new_key[index]) - shift_lower) + symb_count) % symb_count + shift_lower)
            elif symbol.isupper():
                final += chr((ord(symbol) - shift_upper + (ord(new_key[index]) - shift_lower) + symb_count) % symb_count + shift_upper)
            else:
                final += symbol
        else:
            if symbol.islower():
                final += chr((ord(symbol) - shift_lower - (ord(new_key[index]) - shift_lower) + symb_count) % symb_count + shift_lower)
            elif symbol.isupper():
                final += chr(((ord(symbol) - shift_upper - (ord(new_key[index]) - shift_lower) + symb_count) % symb_count) + shift_upper)
            else:
                final += symbol
    return final

def hash_(text):
    "hash some text using standard sha256"
    result = sha256(bytes(text, encoding='utf-8'))
    return result.hexdigest()
