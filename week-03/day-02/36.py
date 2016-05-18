numbers = [3, 4, 5, 6, 7]

def revert(input):
    revrese = []
    for i in range(len(input)-1,-1,-1):
        revrese += [input[i]]
    return revrese

print(revert(numbers))
