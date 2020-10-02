import socket

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

username = 'send'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.setblocking(False)

user = username.encode('utf-8')
username_header = f"{len(user):<{HEADER_LENGTH}}".encode('utf-8')
client.send(username_header + user)

while True:
    message = input(f'Say > ')

    if message:
        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client.send(message_header + message)
