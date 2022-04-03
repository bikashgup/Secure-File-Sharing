#!usr/bin/python

import sys
#from gcd import gcd
#from key_generator import generating_keys

def modinv(e, phi):
     d = 0
     x1 = 0
     x2 = 1
     y1 = 1
     temp_phi = phi
     while (e > 0):
         quo = temp_phi//e
         rem= temp_phi - quo * e
         temp_phi = e
         e = rem
         x = x2- quo* x1
         y = d - quo * y1
         x2 = x1
         x1 = x
         d = y1
         y1 = y
     if (temp_phi == 1 and d>0):
         return (d)
     elif(temp_phi == 1 and d<0):
         return (d+phi)
     
    
