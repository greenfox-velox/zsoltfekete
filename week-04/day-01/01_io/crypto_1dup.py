 # Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    result= ''
    original = f.readlines()
    for y in original:
            for x in range( 0, len(y), 2):
                result += y[x]
    f.close()
    return result
