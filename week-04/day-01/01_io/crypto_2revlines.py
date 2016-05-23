# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    result = ''
    original = f.readlines()
    for y in original:
        y = y.rstrip()
        short_line= y[::-1]
        result += short_line + '\n'
    f.close()
    return result
