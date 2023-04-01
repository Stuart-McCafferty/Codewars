import string

def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)
    text = text.lower()
    result = ""
    find_index = ""
    position = 0
    for i in range(len(text)):
        if text[i] in alphabet:
            position = alphabet.index(text[i]) + 1
            result += str(position) + " "
    return result[:-1]

