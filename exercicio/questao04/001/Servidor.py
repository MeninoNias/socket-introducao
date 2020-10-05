import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)

udp.bind(orig)

print('SERVIDOR STARTADO NO IP {} NA PORTA {}'.format(HOST, PORT))

while True:
    msg, cliente = udp.recvfrom(1024)

    print(cliente, msg.decode())

    cliente_msg = msg.upper().decode()
    udp.sendto(cliente_msg.encode(), cliente)

    if msg is False:
        break

udp.close()