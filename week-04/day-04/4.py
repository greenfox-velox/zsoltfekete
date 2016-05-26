# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def function_squared(x,y):
    final_value = 0
    squared = y
    if y <= 1 :
        return x
    else:
        value = x
        next_step = y - 1
        final_value = value
        return value * function_squared(x,next_step)

print(function_squared(2,1))
print(function_squared(2,5))
print(function_squared(3,3))
print(function_squared(4,4))
print(function_squared(5,5))
print(function_squared(6,6))
