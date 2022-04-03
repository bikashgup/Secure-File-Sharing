import sys,os

def f_expo(data,key,n):
    temp = bin(key)[2:]
    result=1
    i=len(temp)-1
    while i>=0:
        if(temp[i]=='1'):
            result=(result*data)%n
        data=(data*data)%n
        i=i-1 
    return result
#print (f_expo(47,43,77))

        
    
