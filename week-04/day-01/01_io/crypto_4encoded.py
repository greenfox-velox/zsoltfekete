# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = ''
    original = f.read()
    for x in original:
        chr(n) = chr (x) -chr(1)
        result += chr(n)
    return result
