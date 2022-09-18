class Circle:
    def getRadius(self):
        self.radius = int(input("Enter the radius of the circle: "))
        return self.radius

    def AreaOfCircle(self):
        return (self.radius**2)*3.14


class Cylinder(Circle):
    def __init__(self):
        self.height = int(input("Enter the height of the cylinder: "))
        self.radius = super().getRadius()

    def VolumeOfCylinder(self):
        return super().AreaOfCircle()*self.height

    def __str__(self):
        return "The volume of the cylinder is {0}".format(self.VolumeOfCylinder())


cylinder = Cylinder()
print(cylinder)
