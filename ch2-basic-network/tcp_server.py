import socket
import threading
import sys 

IP = "127.0.0.1"
PORT = 8686

html_response = """/
HTTP/1.1 200 OK 
Content-Type: text/html

<html>
  <head><title>server</title></head>
  <body>
      <h1>Hello from Python Server</h1>
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
        
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.sendall(html_response.encode())
if __name__ == '__main__':
    main()