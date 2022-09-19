from abc import ABC, abstractmethod


class Employee(ABC):
    def nameOfEmployee(self):
        self.name = input("Enter name of employee: ")

    @abstractmethod
    def calculateSalary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self):
        super().nameOfEmployee()
        self.salary = int(input("Enter salary of employee: "))

    def calculateSalary(self):
        return self.salary

    def __str__(self):
        return "Employee name is " + self.name + " and salary is " + str(self.salary)


class HourlyEmployee(Employee):
    def __init__(self):
        super().nameOfEmployee()
        self.hours = int(input("Enter hours worked: "))
        self.rate = int(input("Enter rate per hour: "))

    def calculateSalary(self):
        return self.hours * self.rate

    def __str__(self):
        return "Employee name: " + self.name + " Salary: " + str(self.calculateSalary())


class PayRollSystem:
    def __init__(self):
        self.employeeList = []

    def addEmployee(self, *employee):
        self.employeeList.extend(employee)

    def calculatePayRoll(self):
        for employee in self.employeeList:
            print(employee)


emp1 = FullTimeEmployee()
emp2 = HourlyEmployee()


lst = PayRollSystem()

lst.addEmployee(emp1, emp2)

lst.calculatePayRoll()
# print(emp1)
# print(emp2)
