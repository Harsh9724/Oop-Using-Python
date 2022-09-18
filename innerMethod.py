class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop():
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            return self.brand, self.cpu, self.ram


s1 = Student('Dhiman', 25)
s2 = Student('Subhas', 26)

s1.show()

laptop = s1.lap
laptop2 = s2.lap

print(laptop.show())
