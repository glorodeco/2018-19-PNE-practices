import socket
from Seq import Seq


IP = "212.128.253.74"
PORT = 8081
MAX_OPEN_REQUESTS = 200


# A function for validating the sequence

def validsequence(seq):

    valid_aminoacids = ["A", "C", "T", "G"]

    for s in seq:
        if s not in valid_aminoacids:
            return False

    return True


def operation(seq, function):

    if function == "len":
        return seq.len()
    elif function == "complement":
        sequence = seq.complement()
        return sequence.strbases
    elif function == "reverse":
        sequence = seq.reverse()
        return sequence.strbases
    elif function[:-1] == "count":
        return seq.count(function[-1])
    elif function[:-1] == "perc":
        return seq.perc(function[-1])


# A function to read the client requests

def client_proccess(clientsocket):

    # Read the message from the client and decode it as a string

    msg = clientsocket.recv(2048).decode("utf-8")

    print("Message from client: {}".format(msg))

    if msg == "\n":
        response = "ALIVE!"
    else:
        msg = msg.split("\n")
        if validsequence(msg[0].upper()):
            response = "OK"
            seq = Seq(msg[0])
            data = operation(seq, msg[-1].lower())
            response = response + "\n" + str(data)
        else:
            response = "ERROR"

    # Once we finished iterating the message will be send to the client
    clientsocket.send(str.encode(response))


# MAIN PROGRAM

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Become a server socket
serversocket.bind((IP, PORT))

# Configure the server socket
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)


# Accept connections from outside
print("Waiting for connections at {}, {} ".format(IP, PORT))
(clientsocket, address) = serversocket.accept()

# Connection received. A new socket is returned for communicating with the client
print("Attending connections from client: {}".format(address))

client_proccess(clientsocket)

clientsocket.close()

