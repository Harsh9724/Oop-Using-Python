class name:
    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())


obj = name()
obj.getString()
obj.printString()
