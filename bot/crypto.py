"module which contains some crypto functions"
from hashlib import sha256

def caesar(text, key, decode=False):
    "encode or decode message using caesar cipher"
    final = ""
    for symbol in text:
        if not decode:
            if symbol.islower():
                final += chr((ord(symbol) - 97 + key + 26) % 26 + 97)
            elif symbol.isupper():
                final += chr((ord(symbol) - 65 + key + 26) % 26 + 65)
            else:
                final += symbol
        else:
            if symbol.islower():
                final += chr((ord(symbol) - 97 - key + 26) % 26 + 97)
            elif symbol.isupper():
                final += chr(((ord(symbol) - 65 - key + 26) % 26) + 65)
            else:
                final += symbol
    return final

def vigenere(text, key, decode=False):
    "encode or decode text using vigenere cipher"
    final = ""
    new_key = ''
    i, j = 0, 0

    while i < len(text):
        while j < len(key):
            if i < len(text) and j < len(key):
                new_key += text[i]
                i += 1
            elif i < len(text) and j < len(key):
                new_key += key[j]
                i += 1
                j += 1
            else:
                break
        j = 0

    for index, symbol in enumerate(text):
        if not decode:
            if symbol.islower():
                final += chr((ord(symbol) - 97 + (ord(new_key[index]) - 97) + 26) % 26 + 97)
            elif symbol.isupper():
                final += chr((ord(symbol) - 65 + (ord(new_key[index]) - 97) + 26) % 26 + 65)
            else:
                final += symbol
        else:
            if symbol.islower():
                final += chr((ord(symbol) - 97 - (ord(new_key[index]) - 97) + 26) % 26 + 97)
            elif symbol.isupper():
                final += chr(((ord(symbol) - 65 - (ord(new_key[index]) - 97) + 26) % 26) + 65)
            else:
                final += symbol
    return final

def hash_(text):
    "hash some text using standard sha256"
    result = sha256(bytes(text, encoding='utf-8'))
    return result.hexdigest()
