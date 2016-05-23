 # Create a method that decrypts texts/reversed_zen_order.txt

def decrypt(file_name):
    f = open(file_name)
    original = f.readlines()[::-1]
    result = "".join(original)
    f.close()
    return result
