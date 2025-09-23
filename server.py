import socket
ssocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = socket.gethostname() 
port  = 8000

ssocket.bind((host,port))
print(f"server is bound to {host}:{port}")

ssocket.listen(5)
print(f"server is ready to listen with size of 5 clint in client_quese")


print("waiting to accept client")
client,addr = ssocket.accept()
print(f"Got a connection from {addr}")




