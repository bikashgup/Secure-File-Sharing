import socket
import pickle
from encryption import *

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    m= encryption()
    pri_key,pub_key,n=m.generating_keys(1)
    
    filename = raw_input("Filename? -> ")
    
    if filename != 'q':
        data=[filename,pub_key,n]
        msg=pickle.dumps(data)
        s.send(msg)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                msg=m.decrypt(data,pri_key,n)
                totalRecv = len(msg)
                f.write(msg)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(msg)
                    f.write(msg)
                    print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done")
                print ("Download Complete!")
                f.close()
        else:
            print ("File Does Not Exist!")

    s.close()
    

if __name__ == '__main__':
    Main()

