class Rectangle:
    def __init__(self):
        self.width = int(input("Enter the width of the rectangle: "))
        self.height = int(input("Enter the height of the rectangle: "))

    def Perimeter(self):
        return 2 * (self.width + self.height)

    def Area(self):
        return self.width * self.height

    def display(self):
        print("\nlength: ", self.width)
        print("width: ", self.height)
        print("\nThe perimeter is: ", self.Perimeter())
        print("The area is: ", self.Area())


rect = Rectangle()
rect.display()
