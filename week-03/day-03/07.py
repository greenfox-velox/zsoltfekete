# create a function that takes a list and returns a new list with all the elements doubled
ag = [3, 4, 5, 6, 7]

### value double ###
def value_double(value):
    k = []
    for i in value:
        k += [i * 2]
    return k
print(value_double(ag))

### element double ###
def element_double (input):
    return input * 2
print(element_double(ag))
