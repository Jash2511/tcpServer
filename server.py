import socket
import threading

ssocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = socket.gethostname() 
port  = 8000

ssocket.bind((host,port))
print(f"server is bound to {host}:{port}")

ssocket.listen(5)
print(f"server is ready to listen with size of 5 clint in client_quese")


#print("waiting to accept client")
#client,addr = ssocket.accept()
#print(f"Got a connection from {addr}")

def handle_client(client , addr) :
    print(f"[NEW CONNECTION] {addr} connected ")

    message = client.recv(1024).decode('utf-8')
    print(f"[ {addr} ] says : {message} ")

    clinet.send("Thanks! message recived".encode('utf-8'))
    
    client.close()
    print(f"[CONNECTION CLOSED] {addr} disconnected.")

while True :
    print("waiting to accept client")

    client , addr = ssocket.accept()

    print("connected to [{addr}]")
    
    thread = threading.Thread(target=handle_client , args=(client , addr))
    print('assign new thread to handle [{addr}]')
    
    thread.start()




