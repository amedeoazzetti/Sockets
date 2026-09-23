import socket

host = "127.0.0.1"
porta = 6767 # Porta a cui connettersi

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client_socket.bind() non serve a nulla 

client_socket.connect((host, porta))
client_socket.sendall("ciao".encode()) 