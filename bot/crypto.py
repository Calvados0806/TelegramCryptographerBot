"module which contains some crypto functions"
from hashlib import sha256

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
