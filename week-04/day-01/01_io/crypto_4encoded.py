# Create a method that decrypts texts/encoded_zen_lines.txt

def decrypt(file_name):
    f = open(file_name)
    number = ''
    original = f.read()
    f.close()
    for x in original:
        if x == ' ' or x == '\n':
            number += x
        else:
            number += chr(ord(x)-1)
    return number
