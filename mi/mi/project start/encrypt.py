#!usr/bin/python

import sys
from key_generator import *
from fast_exponentiaton import *
def encrypt(data,pub_key,n):
    cipher = pow(data,pub_key,n)
    return cipher
def decrypt():
    pub_key,pri_key,n= generating_keys()
    cipher = encrypt(5000000,pub_key,n)
    decipher = pow(cipher,pri_key,n)
    return decipher
print(decrypt())

