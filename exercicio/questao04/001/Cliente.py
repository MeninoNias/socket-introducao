import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Para sair digite "exit"\n')

msg = str(input("Digite alguma palavra: "))

while msg != "exit":
    udp.sendto(msg.encode(), dest)
    messagem, server = udp.recvfrom(2048)

    if messagem is False:
        break
    print(messagem.decode())

    msg = str(input("Digite alguma palavra: "))

udp.close()