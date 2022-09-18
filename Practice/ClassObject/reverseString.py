class reverseString:
    def getString(self):
        self.s = input("Enter a string: ")

    def reverse(self):
        print(self.s[::-1])


obj = reverseString()
obj.getString()
obj.reverse()
