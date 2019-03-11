import socket

IP = "212.128.253.74"
PORT = 8081

# Ask the user for the string
msg =

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# We receive the information from the server, and then we print it
response = s.recv(2048).decode("utf-8")

# Print server response
print("Response: {}".format(response))