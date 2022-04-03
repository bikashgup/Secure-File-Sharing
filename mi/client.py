import sys,socket,pickle
from encryption import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9998
m=encryption()
pub_key,pri_key,n= m.generating_keys(1)
s.connect((host,port))
data=['hello',pub_key,n]
msg=pickle.dumps(data)
s.send(msg)
msg=s.recv(4096)
data=pickle.loads(msg)
message=m.decrypt(data[0],pri_key,n)
print(message)
s.close()

