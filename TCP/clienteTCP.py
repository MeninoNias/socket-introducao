import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 12345))

menssage_envio = input("Digite a messagem: ")

cliente.send(menssage_envio.encode())

messagem_bytes = cliente.recv(2048)
print(messagem_bytes.decode())
