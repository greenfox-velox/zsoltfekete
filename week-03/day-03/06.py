
numbers=[5,3,5,7,8,9]

def reverse(input):
    reverse= []
    for i in range(len(input)-1,-1,-1):
        reverse += [input[i]]
    return reverse

print(reverse(numbers))
