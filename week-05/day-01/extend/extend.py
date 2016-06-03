# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b > a and b >= c:
        return b
    else:
        return c

# Returns the median value of a list given as param
def median(pool):
    sorted_list= sorted(pool)
    if len(sorted_list) % 2 != 0:
        return sorted_list[int(((len(sorted_list))-1) / 2) + 1]
    else:
        return (sorted_list[int((len(sorted_list)-1)/2)]+sorted_list[int((len(sorted_list)+1)/2)]) /2

print(median([3,5,1,3]))
print(median([1,1,1,3,1,5,1]))
print(median([1,1,3,3,1,4,1]))
print(median([1,1,3,3,3,13,1]))

# Returns true if the param is a vovel
def is_vovel(char):
    if char in 'aeiou':
        return True
    else:
        False
# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    new_world =''
    for char in teve:
        if is_vovel(char):
            new_world += (char+'v'+char)
        else:
            new_world += char
    return new_world
