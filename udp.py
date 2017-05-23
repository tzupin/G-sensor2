import socket

ip="192.168.0.104"
port=8000

msg="hellllllllllllllllllllllllo"
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a=[i for i in range(100)]

while(1):
    sock.sendto(msg,(ip,port))  
