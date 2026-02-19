class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def roll(self):
        print("Wheels rolling")

class Car(Engine, Wheels):
    pass

c = Car()
c.start()
c.roll()
