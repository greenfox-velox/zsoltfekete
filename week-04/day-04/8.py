# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.
def remove(n):
    if len(n) <= 1:
        if n == 'x' :
            return ''
        else:
            return n

    else:
        if n[0] == 'x' :
            return '' + remove(n[1:])
        else:
            return n[0] + remove(n[1:])

print(remove('lxxxxxxoxxxxxl'))
