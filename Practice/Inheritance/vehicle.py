class Vehicle:
    def __init__(self):
        self.typeOfVehicle = input("Enter the type of vehicle: ")
        self.engineNo = input("Enter the engine number of the vehicle: ")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.nameOfCompany = input("Enter the name of the company: ")


class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.maneuverability = input("Enter the maneuverability of the car: ")

    def __str__(self):
        return "\nThe type of the vehicle is {0}.\nThe engine number of the vehicle is {1}.\nThe name of the company is {2}.\nThe maneuverability of the car is {3}".format(self.typeOfVehicle, self.engineNo, self.nameOfCompany, self.maneuverability)


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.capacity = int(input("Enter the capacity of the truck: "))

    def __str__(self):
        return "\nThe type of the vehicle is {0}.\nThe engine number of the vehicle is {1}.\nThe capacity of the truck is {2}".format(self.typeOfVehicle, self.engineNo, self.capacity)


sportCar = SportsCar()
print(sportCar)

truck = Truck()
print(truck)
