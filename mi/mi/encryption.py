#!/usr/bin/python
import sys,os,random

class encryption:
    
    def _init_(self):
        pass
    """
    gen_prime() helps to generate prime number randomly of any size.

    """

    def gen_prime(self):
        prime = int.from_bytes(os.urandom(64),byteorder="little")
        while True:
            if ((prime&1)==0):#it checks whether random no. is even or not
                prime = int.from_bytes(os.urandom(64),byteorder="little")
            else:
                break
        while (True):
            if((self.isprime(prime))==True):
                return prime   
            else:
                prime+=2

                
    '''
    isprime() uses Miller-Rabin primality test to check whether given number is
    prime or not.It is a probabilistic algorithm i.e. there is a chance that it 
    might show a composite number as a prime numbe.This composite number is 
    known as strong psuedoprimes.

    '''        
    def isprime(self,prime):
        secu_para=random.randrange(20,80)
        #secu_para helps to increase the accuracy of this test 
        r=prime-1
        s=0
        while((r&1)==0):#it runs untill r is even
            #we divide the odd number in the form 2^s.r where r is odd
            s+=1
            r>>=1
        for i in range(secu_para):
            rand = random.randrange(2,(prime-2))
            res=pow(rand,r,prime)
            if((res != 1) and (res != (prime-1))):
                j=1
                while((j<=(s-1)and (res != prime-1))):
                    res =pow(res,2,prime)
                    if(res==1):
                        return False
                    j+=1
                if(res != prime-1):
                    return False
        return True

    def gcd(self,x, y):
        #It helps to grestest common divisor
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
    '''
    def f_expo(self,data,key,n):
        temp = bin(key)[2:]
        result=1
        i=len(temp)-1
        while i>=0:
            if(temp[i]=='1'):
                result=(result*data)%n
            data=(data*data)%n
            i=i-1 
        return result
    '''
    def modinv(self,e, phi):
        #calcultes the modulo inverse using extended euclidean algorithm
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
            return d
        elif(temp_phi == 1 and d<0):
            return (d+phi)

    def generating_keys(self,i):
        #we generate private and public for RSA encryption
        
        p = self.strg_prime()
        q = self.strg_prime()
        while (p==q):
            q=self.strg_prime()
            #print(len(str(p)))  
            # print(len(str(q))) 
        n = p*q
        phi_func = (p-1)*(q-1)
        rand = random.randrange(1,64)
        key = int.from_bytes(os.urandom(rand),byteorder="little")
        g = self.gcd(key, phi_func)
        while (g!=1 and key<phi_func):
            rand = random.randrange(1,64)
            #print (key)
            key = int.from_bytes(os.urandom(rand),byteorder="little")
            g = self.gcd(key, phi_func)
        #print(key)    
        d=self.modinv(key,phi_func)
        pub_key = key 
        pri_key = d
        #print(pub_key)
        return pri_key,pub_key,n
    

    def strg_prime(self):
        p=self.gen_prime()
        q=self.gen_prime()
        while (p==q):
            q=self.gen_prime()
        rand1 = random.randrange(1,100)
        rand2= random.randrange(1,100)
        while True:
            p1=2*rand1*q+1
            if (self.isprime(p1)==True and p1!=p):
                break
            rand1+=1
        p0=2*pow(p,p1-2,p1)*p-1
        while True:
            p2=2*rand2*p1*p+p0
            if (self.isprime(p2)==True):
                break
            rand2+=1
        return p2
    def keys():
        pub_key,pri_key,n=generating_keys(1)
        return pub_key,pri_key,n
    def encrypt(self,message,pub_key,n):
        #print(pub_key,n)
        #pri_key=str(pri_key)
        
        #pri_key =pri_key.encode('utf-8')
        
        m=message.encode('utf-8')
        #print(m)
        msg=int.from_bytes(m,byteorder="little")
        #print(msg)
        cipher= pow(msg,pub_key,n)
        #cipher=str(cipher)
        #cipher=cipher.encode('utf-8')    
        #n=str(n)
        #n=n.encode('utf-8')
        return cipher
    
    
    def decrypt(self,cipher,pri_key,n):
        #pub_key,pri_key,n= self.generating_keys(1)
        
        #cipher=int(cipher.decode('utf-8'))
        #pri_key=int(pri_key.decode('utf-8'))
        #n=int(n.decode('utf-8'))
        decipher = pow(cipher,pri_key,n)
        k=decipher.bit_length()
        if(k%8>=5):
            k=k//8+1
        msg=decipher.to_bytes(k,byteorder="little")
        #print (msg)
        message=msg.decode('utf-8')
        return message

c = encryption()
pub_key,pri_key,n=c.generating_keys(1)
p=(c.encrypt("hi",pub_key,n))
print(p)
print(c.decrypt(p,pri_key,n))
    



    
    
        
        
        
