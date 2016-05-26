# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def summa(n):
    if n <= 0:
        return 0
    else:
        return n + summa (n-1)

print(summa())
