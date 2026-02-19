class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

s = Student("Saveliy", 18)
print(s.name)
print(s.age)
