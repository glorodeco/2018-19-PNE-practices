# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)
f= open("person.json", 'r')
person=  json.load(f)

for elem in person:
    termcolor.cprint('Name: ', 'green', end='')
    print(elem['FirstName'], elem['Lastname'])

    termcolor.cprint('Age: ', 'green', end='')
    print(elem['Age'])

    for i, num in enumerate(elem['Phonenumber']):
        termcolor.cprint('Phone {}:'.format(i),'yellow')
        termcolor.cprint("  Type: ",'blue', end='')
        print(num['type'])


        termcolor.cprint("  Number: ", 'blue', end='')
        print(num['number'])
