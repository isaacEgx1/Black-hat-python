import socket 
target_host = "www.google.com"
target_port = 80 

#create a socket object 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the s object
s.connect((target_host,target_port))

#send some data 
s.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

#receive some data 
response = s.recv(4096)

print(response.decode())
s.close()