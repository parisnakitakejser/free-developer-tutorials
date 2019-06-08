import socket

headersize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()


    msg = 'Welcom to socket server - this is a longer test to get more stream to the socket server and client'
    msg = f'{len(msg):<{headersize}}'+ msg

    print(msg)

    print(f'Connection from {address} is now connected')
    clientsocket.send(bytes(msg, 'utf-8'))