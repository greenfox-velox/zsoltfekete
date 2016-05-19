# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student ():
  def __init__(self):
    self.grades = []

  def add_grade(self, grade):
    if grade >= 1 and grade <= 5:
        self.grades += [grade]

  def get_avarage(self):
    return sum(self.grades)/len(self.grades)


jozsi = Student()
geza = Student()
bela = Student()

jozsi.add_grade(5)
jozsi.add_grade(3)
jozsi.add_grade(1)
jozsi.add_grade(2)
bela.add_grade(1)
bela.add_grade(3)
bela.add_grade(1)
bela.add_grade(4)
geza.add_grade(3)
geza.add_grade(2)
geza.add_grade(2)

print(jozsi.get_avarage())
print(geza.get_avarage())
print(bela.get_avarage())
