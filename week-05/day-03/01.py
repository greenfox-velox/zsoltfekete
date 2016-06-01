# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0
def div_ten(number):
    try:
        output = 10 / number
        return output
    except ZeroDivisionError:
        print ('fail')

print(div_ten(5))
div_ten(0)
