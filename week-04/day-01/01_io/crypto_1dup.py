# Create a method that decrypts the texts/duplicated_chars.txt
def decrypt(file_name):
    f = open(file_name)
    result= ''
    file_lines = f.readlines()
    f.close()
    for line in file_lines:
            for index in range( 0, len(line), 2):
                output += line[index]
    return result
