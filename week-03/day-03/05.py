
# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods
class Stack ():
    def __init__(self):
        self.elements = []

    def size(self):
        i = 0
        for element in self.elements:
            i += 1
        return i

    def push(self, add):
        self.elements += [add]

    def pop(self):
        prepop =self.elements[-1]
        self.elements = self.elements[0:-1]
        return prepop

list1=Stack()
list2=Stack()
list3=Stack()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
print(list1.elements)
print(list1.pop())
print(list1.elements)
