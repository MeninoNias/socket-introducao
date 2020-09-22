import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    menssage_envio = input("Digite a messagem: ")
    client.sendto(menssage_envio.encode(), ('192.168.0.104', 12000))
    messagem_bytes, endereco_servidor = client.recvfrom(2048)
    print(messagem_bytes.decode())
