import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

headersize = 10

full_msg = b''
new_msg = True

while True:
    msg = s.recv(16)

    if new_msg:
        print(f'new message len: {msg[:headersize]}')
        msglen = int(msg[:headersize])
        new_msg = False

    print(msg)
    full_msg += msg

    if len(full_msg) - headersize == msglen:
        print('full msg recvd')
        d = pickle.loads(full_msg[headersize:])
        print(d)
        print('#####')
        print(d['Hello'])

        new_msg = True
        full_msg = b''