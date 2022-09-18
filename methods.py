class Students:
    school = "NUV"
    degree = "B.Tech"

    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    @classmethod
    def schoolInfo(name):
        print("School Name: ", name.school)
        return name.school

    @staticmethod
    def degreeInfo():
        Students.school = "Parth"
        return Students.school


s1 = Students(78, 89, 97)
# s2 = Students(77, 92, 85)

# print(int(s1.avg()))
# print(int(s2.avg()))
print(Students.schoolInfo())
print(Students.degreeInfo())
print(Students.schoolInfo())

# from datetime import date as dt


# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def isAdult(age):
#         if age > 18:
#             return True
#         else:
#             return False

#     @classmethod
#     def empFromYear(empClass, name, year):
#         return empClass(name, dt.today().year - year)

#     def __str__(self):
#         return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


# e1 = Employee('Dhiman', 25)
# print(e1)
# e2 = Employee.empFromYear('Subhas', 1987)
# print(e2)
# print(Employee.isAdult(25))
# print(Employee.isAdult(16))
