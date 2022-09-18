class A:
    def f1():
        print("A.f1")


class B:
    def f2():
        print("B.f2")


class C(A, B):
    def f3():
        print("C.f3")
        A.f1()


ob = C()

C.f3()
