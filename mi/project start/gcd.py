#!usr/bin/python

import sys

def gcd(x, y):
    if(x<0):
        x=-x
    if (y<0):
        y=-y
    if((x+y)==0):
        print("Error")
    g=y;
    while (x>0):
        g=x
        x=y%x
        y=g
    return g
#print(gcd(151891622037719395842858147725261272559305802,52654337301074646929663854941618014029091871))





