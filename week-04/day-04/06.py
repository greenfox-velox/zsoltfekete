# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).
def bunny(n):
    if n <= 0:
        return 0
    else:
        next_bunny= (n-1)

        if next_bunny % 2 == 0:
            return 2 + bunny(next_bunny)

        else:
            return 3 + bunny(next_bunny)

print(bunny(1))
print(bunny(2))
print(bunny(3))
print(bunny(4))
print(bunny(5))
