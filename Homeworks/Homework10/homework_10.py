# Завдання 1
print("Завдання 1:")
import math

class Employee:

    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department

class Developer(Employee):

    def __init__(self, name, salary, programming_language, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, team_size, programming_language):
        super().__init__(name, salary, department=department, programming_language=programming_language)
        self.team_size = team_size

manager = Manager(name="Nazar", salary="$3000", department="IT")
developer = Developer(name="Yaroslav", salary="$5000", programming_language="Python")
teamlead = TeamLead(name="Ostap", salary="$10000", department="IT", team_size=10, programming_language="Python")

print(teamlead.name)
print(teamlead.salary)
print(teamlead.department)
print(teamlead.programming_language)
print(teamlead.team_size)


# Завдання 2
print("\nЗавдання 2:")
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        pi = 3.14
        return round(pi * self.__radius ** 2, 2)

    def perimeter(self):
        pi = 3.14
        return round(2 * pi * self.__radius, 2)

class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return round(math.sqrt((p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))), 2)

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

shapes = [
    Circle(5),
    Rectangle(10, 10),
    Triangle(3, 4, 5)
]

for i in shapes:
    print(f"{i.__class__.__name__}: area = {i.area()}, perimeter = {i.perimeter()}")