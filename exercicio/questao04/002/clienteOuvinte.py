import socket
import errno
import sys

IP = '127.0.0.1'
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = str('recive').encode('utf-8')
client.sendto(message, (IP, PORT))

print("Aguardando menssagem do servidor...")

while True:
    message_server, server = client.recvfrom(2048)
    message = message_server.decode()
    print(message)

