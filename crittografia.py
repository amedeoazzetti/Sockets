import socket

key = 3
porta = 6767
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", porta))
server_socket.listen(1)

def decifra(strin):
    # Implement the decryption logic here
    decrypted = ""
    for char in strin:
        decrypted += chr((ord(char) - key) % 256)
    return decrypted

while True:
    print("In attesa di connessione...")
    client_socket, addr = server_socket.accept()
    print(f"Connessione accettata da {addr}")

    data = client_socket.recv(1024)
    if not data:
        break

    decrypted_message = decifra(data.decode())
    print(f"Messaggio ricevuto: {decrypted_message}, messaggio originale: {data.decode()}")

    client_socket.close()
