class A:
    def __init__(self, paramA) -> None:
        self.paramA = paramA

    def simpan(self, paramA):
        print(self, paramA)

class B(A):
    def __init__(self, paramA, 
        paramB):
        self.paramB = paramB
        A.__init__(self, paramA)

    def simpan(self):
        print(self.paramA, self.paramB )

b_obj = B('a', 'b')
b_obj.simpan()
