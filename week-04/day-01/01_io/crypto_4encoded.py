# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = ''
    original = f.read()
    for x in original:
        result += chr(x+1)
    return result
