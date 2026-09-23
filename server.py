import socket

host = "127.0.0.1" 
porta = 6767 # Porta in ascolto

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Tcp Ipv4

socket = (host, porta)

server_socket.bind(socket)

server_socket.listen() # socket in ascolto
conn, ip = server_socket.accept() #.accept restituisci una tupla che vengono salvate nelle due variabili dichiarati prima  

# abbiamo la connessione (conn)
bytes = conn.recv(4)

print(bytes.decode())