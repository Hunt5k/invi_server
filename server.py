import socket
import sys
import select


host=''
port = 69

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024

data,addr = s.recvfrom(buf)
print("Received File:",data.strip())
f = open(data.strip(),'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except socket.timeout:
    f.close()
    s.close()
    print ("selesai simpan data")


#s.bind(('192.168.43.3',12345))

#while True:
#    data,addr=s.recvfrom(4096)
#    print(str(data))
#    message=("Hello I am UDP Server ").encode("utf-8")
#   s.sendto(message,addr)

