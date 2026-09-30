import socket

host = "192.168.5.24" 

# Porta in ascolto
porta = 6767

# Tcp Ipv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket = (host, porta)

server_socket.bind(socket)

# socket in ascolto
server_socket.listen()


#.accept restituisci una tupla che vengono salvate nelle due variabili dichiarati prima
conn, ip = server_socket.accept()   

# abbiamo la connessione (conn)
bytes = conn.recv(4)

print(bytes.decode())