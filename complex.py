"""
walid:maintainer
member1:addition, subtraction
member2:multiplication
"""
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    
    def __str__(self):
        return str(self.re)+"+"+str(self.im)+"i"

    def add(self, c1): # (1+2i) + (2+3i) = 3+5i
        c = Complex()
        c.re = self.re + c1.re
        c.im = self.im + c1.im
        return c

    def subtract(self, c1): # (2+3i) - (1+2i) = 1+1i
        c = Complex()
        c.re = self.re - c1.re
        c.im = self.im - c1.im
        return c
        
    def multiply(self, c1): # (a+bi)(c+di)=ac+adi+bci-bd = (ac-bd) + (ad+bc)i
        c = Complex()
        c.re = self.re*c1.re - self.im*c1.im
        c.im = self.re*c1.im + self.im*c1.re
        return c
    
    def __sub__(self, c):
        return self.subtract(c)

    def __add__(self, c): # self + c
        return self.add(c)

c1 = Complex(1,2)
print(c1)
c2 = Complex(2,3)
print(c1+c2)
print(c2-c1)
print(c1.multiply(c2))
