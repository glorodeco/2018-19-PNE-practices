# WE ARE PROGRAMMING OUR FIRST CLIENT

import socket

# CREATE A SOCKET FOR COMMUNICATING WITH THE SERVER
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 8082

    IP="212.128.253.74"

    s.connect((IP, PORT))

    holi = input('Your sequence is:')

    s.send(str.encode(holi))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)
    s.close()


