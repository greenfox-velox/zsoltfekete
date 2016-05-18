numbers = [3, 4, 5, 6, 7]

def filter_odds(input):
    evens = []
    for item in input:
        if item % 2 ==0:
            evens += [item]
    return evens

print(filter_odds(numbers))
