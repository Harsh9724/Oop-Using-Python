class MarksNotInRange(Exception):
    def __init__(self, marks, message="Marks not in range"):
        super().__init__(message)


print("one")
x = 1001
if not 0 <= x <= 100:
    raise MarksNotInRange(x)
print("two")
