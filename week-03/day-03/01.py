# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area
class Circle ():
  def __init__(self, r):
      self.r = r
      self.pi=3.14
  def get_circumference(self):
        return 2 * self.r * self.pi

  def get_area(self):
        return self.pi * (self.r ** 2)

kor1 = Circle(1)
kor2 = Circle(5)

print(kor1.get_circumference())
print(kor1.get_area())


print(kor2.get_circumference())
print(kor2.get_area())
