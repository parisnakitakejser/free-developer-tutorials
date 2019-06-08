import socket
import pickle

headersize = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()


    msg = pickle.dumps({
        'Hello': 'World',
        'Socket': 'Server',
        'Recived': 'Data'
    })

    msg = bytes(f'{len(msg):<{headersize}}', 'utf-8') + msg

    print(msg)

    print(f'Connection from {address} is now connected')
    clientsocket.send(msg)