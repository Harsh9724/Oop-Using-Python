class Person:
    def __init__(self):
        self.name = input("Enter the name of the person: ")
        self.age = int(input("Enter the age of the person: "))


class Company:
    def __init__(self):
        self.cname = input("Enter the name of the company: ")
        self.address = input("Enter the address of the company: ")


class Employee(Person, Company):
    def __init__(self):
        Person.__init__(self)
        Company.__init__(self)
        self.salary = int(input("Enter the salary of the employee: "))
        self.skill = input("Enter the skill of the employee: ")

    def __str__(self):
        return "\nThe name of the person is {0}.\nThe age of the person is {1}.\nThe name of the company is {2}.\nThe address of the company is {3}.\nThe salary of the employee is {4}.\nThe skill of the employee is {5}".format(self.name, self.age, self.cname, self.address, self.salary, self.skill)


emp = Employee()
print(emp)
