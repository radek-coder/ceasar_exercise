def decrypt(cipher_text, offset):
    plain_text_output = ""
    for i in cipher_text:
        numerical_value = ord(i)
        if i.isupper():
            adj = ((numerical_value - offset - 65) % 26) + 65
            plain_text_output += chr(adj)
        elif numerical_value == 32:
            plain_text_output += i
            pass
        else:
            adj = ((numerical_value - offset - 97) % 26) + 97
            plain_text_output += chr(adj)
    return plain_text_output
