# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def string(n):
    letter = n
    output = ''
    for i in (letter):
        if i == 'x' :
            output += 'y'
        else:
            output += i
    return output

print(string('zuiezwtiexxitiut'))

def string2(n):
    if len(n) <= 1:
        if n == 'x' :
            return 'y'
        else:
            return n
    else:
        if n[0] == 'x' :
            return 'y'+ string2(n[1:])
        else:
            return n[0] + string2(n[1:])

print(string2('zuiezwtiexxitiut'))
