import sys,socket,pickle
from encryption import *

serversocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
host=socket.gethostname()
port =9998
serversocket.bind((host,port))
serversocket.listen(5)
e1 = encryption()
while True:
    clientsocket,addr=serversocket.accept()
    while True:
        data=clientsocket.recv(4096)
        data_list=pickle.loads(data)
        print(data_list)
        if(len(data)>0):
            print("Got connection",data_list[0])
            break
        else:
            clientsocket.close()
    pub_key,pri_key,n=e1.generating_keys(1)
    m=" isprime() uses Miller-Rabin primality test to check whether given  number is prime or not.It is a probabilistic algorithm e"
    msg=e1.encrypt(m,data_list[1],data_list[2])
    data=[msg,pub_key,n]
    da = pickle.dumps(data)
    clientsocket.send(da)
    clientsocket.close()
