import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

username = input("Username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.setblocking(False)

user = username.encode('utf-8')
username_header = f"{len(user):<{HEADER_LENGTH}}".encode('utf-8')
client.send(username_header + user)

while True:

    try:
        while True:
            username_header = client.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client.recv(username_length).decode('utf-8')

            message_header = client.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client.recv(message_length).decode('utf-8')

            print(f'{username} > {message}')


    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()