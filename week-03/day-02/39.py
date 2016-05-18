names = ['Zakarias', 'Hans', 'Otto', 'Ole']

def find_minimum(input):
    minimum_word = input [0]
    for item in input:
        if len(item) < len(minimum_word):
            minimum = item
    return minimum
print(find_minimum(names))
