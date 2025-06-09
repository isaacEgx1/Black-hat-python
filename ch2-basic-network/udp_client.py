import socket

target_host = "127.0.0.1"
target_port = 80

#create a socket object 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data 
s.sendto(b"AAAABBB",(target_host,target_port))

#receive some data 
data , addr = s.recvfrom(4096)
print(data.decode())
s.close()