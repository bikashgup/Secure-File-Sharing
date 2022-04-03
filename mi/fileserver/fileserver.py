import socket
import threading
import os
from encryption import *
import pickle

def RetrFile(name, sock):
    m=encryption()
    filename = sock.recv(6144)
    dat=pickle.loads(filename)
    if os.path.isfile(dat[0]):
        sock.send("EXISTS " + str(os.path.getsize(dat[0])))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(data[0]) as f:
                bytesToSend = f.read(1024)
                msg= m.encrypt(bytesToSend,dat[1],dat[2])
                sock.send(msg)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    msg= m.encrypt(bytesToSend,dat[1],dat[2])            
                    sock.send(msg)
    else:
        sock.send("ERR ")

    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print ("Server Started.")
    while True:
        c, addr = s.accept()
        print ("client connedted ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()

