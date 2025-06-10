import socket
import threading
import argparse
import sys
parser = argparse.ArgumentParser(description="tcp server")
parser.add_argument("-p" , dest="port" , type=int , help="choose which port you want to build the server on from (1024-65,536)")
args = parser.parse_args()
# 127.0.0.1 this is local host in any client
IP = "127.0.0.1"
PORT = args.port

html_response = """/
HTTP/1.1 200 OK 
Content-Type: text/html

<html>
  <head><title>server</title></head>
  <body>
      <h1>Hello from the python server</h1>
  </body>
</html>
"""
def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")
    

    while True:
        cleint , addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        cleint_handler = threading.Thread(target=handle_client, args=(cleint,))
        cleint_handler.start()
        if KeyboardInterrupt:
            sys.exit(0)
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.sendall(html_response.encode())
if __name__ == '__main__':
    main()