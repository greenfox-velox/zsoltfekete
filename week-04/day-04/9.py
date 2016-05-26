# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*"

def star(n):
    if len(n) <= 1:
        return n
    else:
        return (n[0]+'*') + star(n[1:])

print(star('lxxxxxxoxxxxxxxxl'))
