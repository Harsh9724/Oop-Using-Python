class Maths:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def pow(self):
        print(self.x ** self.n)


maths = Maths(100, 10)
maths.pow()
