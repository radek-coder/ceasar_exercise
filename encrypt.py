def encrypt(plain_text, offset):
    cipher_text = ""
    for i in plain_text:
        numerical_value = ord(i)
        if i.isupper():
            adj = ((numerical_value - offset - 65) % 26) + 65
            cipher_text += chr(adj)
        elif numerical_value == 32:
            cipher_text += i
            pass
        else:
            adj = ((numerical_value + offset - 97) % 26) + 97
            cipher_text += chr(adj)
    return cipher_text
