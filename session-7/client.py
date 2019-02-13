# WE ARE PROGRAMMING OUR FIRST CLIENT

import socket

# CREATE A SOCKET FOR COMMUNICATING WITH THE SERVER
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('sOCKET CREATED')

    PORT = 8080

    IP="212.128.253.73"

    s.connect((IP, PORT))

    holi = input('What do you want to say?:')

    s.send(str.encode(holi))

    msg = s.recv(2048).decode('utf-8')
    print('Message from the server')
    print(msg)
    s.close()

    print('The end')

