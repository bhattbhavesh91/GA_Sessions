import pandas as pd
import numpy as np
import math

# https://www.python-course.eu/python3_magic_methods.php

class complex_number:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag<0:
            return '{}-i{}'.format(self.real,abs(self.imag))
        else:
            return '{}+i{}'.format(self.real,self.imag)

    def __add__(self,other):
        c = self.real+other.real
        d = self.imag+other.imag
        return complex_number(c,d)

    def __sub__(self,other):
        c= self.real-other.real
        d= self.imag-other.imag
        return complex_number(c,d)

    def __mul__(self,other):
        c= (self.real*other.real - self.imag*other.imag)
        d= (self.real*other.imag + self.imag*other.real)
        return complex_number(c,d)

    def __truediv__(self,other):
        c= ((self.real*other.real+self.imag*other.imag))/(other.real**2+other.imag**2)
        d= ((self.imag*other.real-self.real*other.imag))/(other.real**2+other.imag**2)
        #return complex_number(c,d)
        return c,d

    def conjugate(self):
        c = self.real
        d = self.imag
        return complex_number(c,-d)
    
    def abs(self):
        c = (self.real**2+self.imag**2)**(1/2)
        return c
    
    def argument(self):
        c = math.degrees(np.arctan(self.real/self.imag))
        return c
    

c1 = complex_number(4,4)
c2 = complex_number(4,-3)
print (c1)
print (c2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.conjugate())
print(c1.abs())
print(c1.argument())