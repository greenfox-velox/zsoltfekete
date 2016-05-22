class Person():
     def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

     def greet(self):
        print(self.last_name + " " + self.first_name)

class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)
        self.grades = []

    def add_grade(self, grade):
            self.grades.append(grade)

    def salute(self):
        self.greet()
        total = 0
        for grade in self.grades:
            total += grade
        print(total / len(self.grades))

Rudi = Student( "Rudi", "Turo")
Rudi.add_grade(1)
Rudi.add_grade(5)
Rudi.add_grade(2)
Rudi.add_grade(5)
Rudi.add_grade(5)
Rudi.salute()
