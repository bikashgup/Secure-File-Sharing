#!usr/bin/python
from gcd import gcd
from strong_prime import *
from extended_euclidean import modinv
import sys,os,random

def generating_keys():
    p = strg_prime()
    q = strg_prime()
    while (p==q):
        q=strg_prime()
    print(len(str(p)))  
    print(len(str(q))) 
    n = p*q
    phi_func = (p-1)*(q-1)
    rand = random.randrange(1,64)
    key = int.from_bytes(os.urandom(rand),byteorder="little")
    g = gcd(key, phi_func)
    while (g!=1 and key<phi_func):
        rand = random.randrange(1,64)
        key = int.from_bytes(os.urandom(rand),byteorder="little")
        g = gcd(key, phi_func)
    d=modinv(key,phi_func) 
    pub_key = key  
    pri_key = d
