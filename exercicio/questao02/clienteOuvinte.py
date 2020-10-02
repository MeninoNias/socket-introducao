import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.setblocking(False)

message = str('recive').encode('utf-8')
message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
client.send(message_header + message)

while True:
    try:
        while True:
            message_header = client.recv(HEADER_LENGTH)

            if not len(message_header):
                print('Connection closed by the server')
                sys.exit()
            message_length = int(message_header.decode('utf-8').strip())
            message = client.recv(message_length).decode('utf-8')

            print(f'{message}')


    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()