import sys,random
#from fast_exponentiaton import *
#from gcd import gcd
def isprime(prime):
    secu_para=random.randrange(20,80)
    r=prime-1
    s=0
    while((r&1)==0):
        s+=1
        r>>=1
    for i in range(secu_para):
        rand = random.randrange(2,(prime-2))
        res=pow(rand,r,prime)
        if((res != 1) and (res != (prime-1))):
            j=1
            while((j<=(s-1)and (res != prime-1))  ):
                res =pow(res,2,prime)
                if(res==1):
                    return False
                j+=1
            if(res != prime-1):
                return False
    return True        
#print(isprime(347092615))      
