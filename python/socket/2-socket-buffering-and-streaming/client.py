import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

headersize = 10

full_msg = ''
new_msg = True

while True:
    msg = s.recv(16)

    if new_msg:
        print(f'new message len: {msg[:headersize]}')
        msglen = int(msg[:headersize])
        new_msg = False

    print(msg.decode('utf-8'))
    full_msg += msg.decode('utf-8')

    if len(full_msg) - headersize == msglen:
        print('full msg recvd')
        print(full_msg[headersize:])

        new_msg = True
        full_msg = ''