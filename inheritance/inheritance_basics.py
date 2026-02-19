class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()



class Person:
    def walk(self):
        print("Person is walking")

class Student(Person):
    pass

s = Student()
s.walk()
