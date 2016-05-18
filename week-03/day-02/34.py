numbers = [4, 5, 6, 7, 8, 9, 10]

def sum_function(input):
    total = 0
    for i in range(1,len(input)):
        total += input[i]
    return total

print(sum_function(numbers))
