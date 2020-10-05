import socket
import _thread

IP = "127.0.0.1"
PORT = 1234

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_sock.bind((IP, PORT))

clientes = {}

print(f'Ouvindo conexões em {IP}: {PORT} ...')

def recive_message():
    try:
        while True:
            data, addr = server_sock.recvfrom(2048)
            message = data.decode()

            changed_message = tranformar_palavra(message)
            server_sock.sendto(changed_message, clientes['recive'])

    except:
        return False

def tranformar_palavra(palavra):
    if palavra:
        r = len(palavra)
        palavra = list(palavra)
        for p in range(r):
            palavra[p] = chr(ord(palavra[p])+1)
        return ''.join(palavra).encode()


while True:
    message_user, user_addr = server_sock.recvfrom(2048)
    print(message_user.decode())
    print("Conexão - {}".format(user_addr))

    clientes[message_user.decode()] = user_addr
    _thread.start_new_thread(recive_message,())
