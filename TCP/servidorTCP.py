import socket

servidor_ip = 'localhost'
servidor_port = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((servidor_ip, servidor_port))
servidor.listen(5)

print("UPL PORT: " + servidor_ip +":"+str(servidor_port))

while True:
    request_client, ip_addrs = servidor.accept()

    request = request_client.recv(2048)

    print(request.decode())

    ip_port_addres = str(ip_addrs[0]+":"+str(ip_addrs[1]))
    messagem_bytes = "\nCONEXÃO ABERTA - " + ip_port_addres + "\nECO: " + request.decode() + "\n"
    request_client.send(messagem_bytes.encode())

    request_client.close()


