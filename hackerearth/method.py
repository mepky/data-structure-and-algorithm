class abc:
        def __init__(self,a,b):
                self.a=a
                self.b=b
        def ab(self):
                return self.a*self.b

a=abc(2,3)
print(a.ab())
