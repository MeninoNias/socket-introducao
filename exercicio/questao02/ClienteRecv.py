import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    cliente.connect(('localhost', 12345))
    menssagem_info = cliente.recv(2048)

    if menssagem_info:
        print(menssagem_info.decode())
    else:
        cliente.close()

    if(menssagem_info.decode().upper()=='EXIT'):
        break

cliente.close()