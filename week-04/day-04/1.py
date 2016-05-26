# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def countdown(n):
    if n <= 0:
        pass
    else:
        print(n)
        countdown(n-1)

countdown(10)

def concat2(n):
    if n <= 0:
        return []
    else:
        return [n] + concat2 (n-1)

print(concat2(99))
