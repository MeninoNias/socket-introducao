import socket

IP = '127.0.0.1'
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setblocking(False)

username = 'send'
user = username.encode('utf-8')
client.sendto(user, (IP, PORT))

while True:
    message = input(f'Say > ')

    if message:
        message = message.encode('utf-8')
        client.sendto(message, (IP, PORT))
