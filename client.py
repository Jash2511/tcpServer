import socket
csocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

csocket.connect((host,port)) 
print(f"Socket is ready to connect at {host}:{port} ")

csocket.send("hey we are oging to see new things".encode('utf-8'))
print('message send to server')

message = csocket.recv(1024).decode('utf-8')
print(f"server says : {message} ")

csocket.close()
print("connection is closed")

