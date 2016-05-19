# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name
# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():
     def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

     def greet(self):
        print(self.last_name + " " + self.first_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grade(self, grade):
        if grade >= 1 and grade <= 5:
            self.grades += [grade]

    def get_average(self):
        return sum(self.grades)/len(self.grades)

    def salute(self):
        print(self.greet(), self.get_average())

Rudi = Student( "Rudi", "Turo")
Rudi.add_grade(1)
Rudi.add_grade(5)
Rudi.add_grade(2)
Rudi.add_grade(5)
Rudi.add_grade(5)
Rudi.salute()
