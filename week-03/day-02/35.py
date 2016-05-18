def factorial(input_number) :
    factorta = 1
    for i in range(1, input_number+1):
        factorta = factorta * i
    return factorta

print(factorial(10))
