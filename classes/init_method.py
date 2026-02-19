class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Ayan")
s2 = Student("Dana")

print(s1.name)
print(s2.name)




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(4, 5)
print(r.width * r.height)
