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
    message = input(f'{username} > ')

    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client.send(message_header + message)


        try:
            while True:

                username_header = client.recv(HEADER_LENGTH)

                # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
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
            # This is normal on non blocking connections - when there are no incoming data, error is going to be raised
            # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
            # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
            # If we got different error code - something happened
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()

            # We just did not receive anything
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()