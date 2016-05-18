
ae = 'Jozsi'
def greet_function(name="Valaki"):
    return "Hello, "+name+"!"

print(greet_function(ae))


#test
def test(expected, actual):
    if expected == actual :
        print("Checked")
    else:
        print("Jaj")

test("Hello, Jozsi!", greet_function(ae))
