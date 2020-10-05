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

            if isnumber(message):
                message = str(int(message) - 1).encode()
            else:
                message = 'INFORME SOMENTE NUMEROS'.encode()
            server_sock.sendto(message, clientes['recive'])

    except:
        return False

def isnumber(value):
    try:
         int(value)
    except ValueError:
         return False
    return True


while True:
    message_user, user_addr = server_sock.recvfrom(2048)
    print("Conexão - {}".format(user_addr))

    clientes[message_user.decode()] = user_addr
    _thread.start_new_thread(recive_message,())
