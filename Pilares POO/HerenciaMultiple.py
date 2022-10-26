class A():
    def primera(self):
        return "esta es la clase A"

class B():
    def segunda(self):
        return "esta es la clase b"

class C(A,B):
    pass

c=C()
print(c.primera())
print(c.segunda())