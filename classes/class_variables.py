class School:
    name = "KBTU"

s1 = School()
s2 = School()

print(s1.name)
print(s2.name)



class Counter:
    count = 0

    def increase(self):
        Counter.count += 1
        print(Counter.count)

c1 = Counter()
c2 = Counter()

c1.increase()
c2.increase()
