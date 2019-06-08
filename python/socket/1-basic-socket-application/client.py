import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


full_msg = ''
while True:
    msg = s.recv(6)

    if len(msg) <= 0:
        break

    print(msg)
    full_msg += msg.decode('utf-8')

print(full_msg)