import socket
import select

HEAD_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_sock.bind((IP, PORT))
server_sock.listen()

list_sock = [server_sock]
clients = {}

print(f'Ouvindo conexões em {IP}: {PORT} ...')

def recive_message(cSockt):
    try:
        message_sock = cSockt.recv(HEAD_LENGTH)
        if not len(message_sock):
            return False

        message_len = int(message_sock.decode('utf-8').strip())
        return {
            "header": message_sock,
            "data": cSockt.recv(message_len)
                }
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
    read_sockts, _, exception_sockts = select.select(list_sock, [], list_sock)

    for nSocks in read_sockts:
        if nSocks == server_sock:
            cliente_sock, cliente_addres = server_sock.accept()

            user = recive_message(cliente_sock)

            if user is False:
                continue

            list_sock.append(cliente_sock)

            clients[cliente_sock] = user
            print("NOVA CONEXÃO ACEITA")
        else:
            message = recive_message(nSocks)

            if message is False:
                print("FECHANDO CONEXÃO")
                list_sock.remove(nSocks)
                del clients[nSocks]
                continue

            message['data'] = tranformar_palavra(message['data'].decode("utf-8"))

            print("RECEBEU UMA MENSSAGEM")

            for client_sock in clients:
                if client_sock != nSocks:
                    client_sock.send(message['header']+message['data'])

    for notified_sock in exception_sockts:
        list_sock.remove(notified_sock)
        del clients[notified_sock]