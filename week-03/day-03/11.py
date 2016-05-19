def diamond(line):
    if line % 2 != 0 :
        row = (line // 2)+1
        space = row-1
        star = 1
        for x in range(1 ,row):
            print ((" " * space),("*" * star))
            star += 2
            space -= 1
        for x in range(row):
            print ((" " * space),("*" * star))
            star -= 2
            space += 1
    else:
        print("Only odd numbers, sorry!")

diamond(15)
