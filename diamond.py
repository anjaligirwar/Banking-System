class A:

    def bags(self):
        print("This is a method of class A")


class B(A):
    def bags(self):
        print("This bags is of B")



class C(A):
    def bags(self):
        print("This method belongs to class C")


class D(C,B):
    pass


d = D()
d.bags()