import socket

host = "127.0.0.1"

# Porta a cui connettersi
porta = 6767 

# Tcp Ipv4
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client_socket.bind() non serve a nulla 
client_socket.connect((host, porta))
client_socket.sendall("ciao".encode()) 