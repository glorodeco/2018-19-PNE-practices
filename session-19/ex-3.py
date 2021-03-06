# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input('Introduce an user: ')
VAR= GITHUB_ID+'/repos'
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID , None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data
login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))

#------------------------------------------------------

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + VAR , None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()



# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
info= json.loads(text_json)
print('-'*10)
print('The repositories are: ')
for element in info:
    # -- Get some data
    name_repos = element['name']

    print(name_repos)

#--------------------------------------
#/repos/Obijuan/2018-19-PNE-practices/contributors
REPOS='/repos/'
FOLD= '/2018-19-PNE-practices'
CONTR= '/contributors'
# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, REPOS + GITHUB_ID + FOLD + CONTR , None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
commits = json.loads(text_json)
times = commits[0]['contributions']
print('-'*10)
print('The times of contributions in the repository 2018-19-PNE-practices is:', times)

