import socket 
import argparse

parser = argparse.ArgumentParser(description="TCP client , Send Request & Receive  Response")
parser.add_argument("-t" ,dest="target", help="target send to request")
parser.add_argument("-p" ,dest="port" ,type=int, help="port")
parser.add_argument("-m" ,dest="method" , help="any method : GET,HEAD,POST,PUT,DELETE,...")
args = parser.parse_args()


target_host = args.target
target_port = args.port
target_method = args.method

#create a socket object 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the s object
s.connect((target_host,target_port))

#send some data 
request = f"{target_method} / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
s.send(request.encode())

#receive some data 
response = s.recv(4096)

print(response.decode())
s.close()