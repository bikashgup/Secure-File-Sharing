import sys,random
from prime_gen import *
from check_prime import *
def strg_prime():
    p=gen_prime()
    q=gen_prime()
    while (p==q):
        q=gen_prime()
    rand1 = random.randrange(1,100)
    rand2= random.randrange(1,100)
    while True:
        p1=2*rand1*q+1
        if (isprime(p1)==True and p1!=p):
            break
        rand1+=1
    p0=2*pow(p,p1-2,p1)*p-1
    while True:
        p2=2*rand2*p1*p+p0
        if (isprime(p2)==True):
            break
        rand2+=1
    return p2
#print(strg_prime())

        
        
