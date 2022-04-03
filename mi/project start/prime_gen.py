import sys,os
from check_prime import isprime 
def gen_prime():
    prime = int.from_bytes(os.urandom(64),byteorder="little")
    while True:
        if ((prime&1)==0):
            prime = int.from_bytes(os.urandom(64),byteorder="little")
        else:
            break
    while (True):
        if((isprime(prime))==True):
            return prime   
        else:
            prime+=2

            
        
        
        
        
        
    
        
    
