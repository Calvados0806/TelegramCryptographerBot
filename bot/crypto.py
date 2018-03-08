def caesar(text, key, decode=False):
    final = ""
    for symbol in text:
        if not decode:
            final += chr((ord(symbol) + key))
        else:
            final += chr((ord(symbol) - key))
    return final

def vigenere(text, key, decode=False):
    final = ""
    key *= len(text) // len(key) + 1
    for index, symbol in enumerate(text):
        if not decode:
            final += chr((ord(symbol) + ord(key[index]) % 26))
        else:
            final += chr((ord(symbol) - ord(key[index]) % 26))
    return final
