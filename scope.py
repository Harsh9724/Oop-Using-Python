
def f():
    def g(a):
        return a+1

    def h(b):
        return b*2

    global x

    y = g(x) + h(x)  # y = (x+1) + (2*x)
    print(y)
    x = 23


x = 4
f()
print(x)
