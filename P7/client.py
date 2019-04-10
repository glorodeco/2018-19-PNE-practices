# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from SeqP1 import Seq


PORT = 80
SERVER = 'rest.ensembl.org'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

headers = {'Content-type': 'text/plain'}

# -- Send the request message, using the GET method.
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
info = json.loads(data1)

FRAT1_seq = Seq(info['seq'])

# -- Length bases in the FRAT1 gen
length = FRAT1_seq.len()

# -- Bases in the FRAT1 gen
T = FRAT1_seq.count('T')
A = FRAT1_seq.count('A')
C = FRAT1_seq.count('C')
G = FRAT1_seq.count('G')
popular_base = ""
if A > T and A > C and A > G:
    popular_base = 'A'
elif T > A and T > C and T > G:
    popular_base = 'T'
elif C > A and C > T and C > G:
    popular_base = 'C'
elif G > A and G > T and G > C:
    popular_base = 'G'

# -- Percentage of the most popular base in the FRAT1 gen
Perc_pop = FRAT1_seq.perc(popular_base)

# -- Percentage of all the bases in the FRAT1 gen
perc_A = FRAT1_seq.perc('A')
perc_T = FRAT1_seq.perc('T')
perc_C = FRAT1_seq.perc('C')
perc_G = FRAT1_seq.perc('G')

# -- Printing the result
print("There are {} bases in the FRAT1 gene.".format(length))
print("There are {} T bases in the FRAT1 gene.".format(T))
print("{} is the most popular base in the FRAT1 gene. With the percentage: {}%".format(popular_base, Perc_pop))
if popular_base == 'A':
    print("Percentage of the base T: {}%".format(perc_T))
    print("Percentage of the base C: {}%".format(perc_C))
    print("Percentage of the base G: {}%".format(perc_G))
elif popular_base == 'T':
    print("Percentage of the base A: {}%".format(perc_A))
    print("Percentage of the base C:  {}%".format(perc_C))
    print("Percentage of the base G: {}%".format(perc_G))
elif popular_base == 'C':
    print("Percentage of the base A: {}%".format(perc_A))
    print("Percentage of the base T: {}%".format(perc_T))
    print("Percentage of the base G: {}%".format(perc_G))
elif popular_base == 'G':
    print("Percentage of the base A: {}%".format(perc_A))
    print("Percentage of the base T: {}%".format(perc_T))
    print("Percentage of the base C: {}%".format(perc_C))