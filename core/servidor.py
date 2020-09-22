import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('',12000))

while True:
    message_bytes, endereco_ip_client = servidor.recvfrom(2048)
    message_resposta = message_bytes.decode().upper()

    servidor.sendto(message_resposta.encode(), endereco_ip_client)
    print(message_resposta)

