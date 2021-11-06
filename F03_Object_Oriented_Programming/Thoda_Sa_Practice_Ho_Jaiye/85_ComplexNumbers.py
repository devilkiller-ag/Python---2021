import math


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c2):
        r = self.real + c2.real
        i = self.imaginary + c2.imaginary

        if(i >= 0):
            return f'{r} + {i}i'
        else:
            return f'{r} - {abs(i)}i'

    def __str__(self):
        if(self.imaginary >= 0):
            return f'{self.real} + {self.imaginary}i'
        else:
            return f'{self.real} - {abs(self.imaginary)}i'

    def __mul__(self, c2):
        r = self.real * c2.real - self.imaginary * c2.imaginary
        i = self.real * c2.imaginary + self.imaginary * c2.real

        if(i >= 0):
            return f'{r} + {i}i'
        else:
            return f'{r} - {abs(i)}i'


c1 = Complex(1, -4)
print('c1 = ', c1)
c2 = Complex(331, -37)
print('c2 = ', c2)
ca = c1 + c2
print('c1 + c2 = ', ca)
cp = c1 * c2
print('c1 x c2 = ', cp)
