def tree(line):
    space = line - 1
    star = 1
    for x in range(1 ,line + 1):
        print ((" " * space),("*" * star))
        star += 2
        space -= 1

tree(88)
