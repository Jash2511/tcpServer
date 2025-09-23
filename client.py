import socket
csocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

csocket.connect((host,port)) 
print(f"Socket is ready to connect at {host}:{port} ")

csocket.close()
print("connection is closed")

