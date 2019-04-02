import http.client
import json

# -- API information


#def retrievewoeid (city):


HOSTNAME = "www.metaweather.com"
METHOD = "GET"


# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
conn = http.client.HTTPSConnection(HOSTNAME)

aa= True
woeid=0
city = input('Introduce your city: ')
while aa:

    ENDPOINT = "/api/location/search/?query={}".format(city)
    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

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
    weather = json.loads(text_json)

    if len(weather)==0:
        print('Your capital is not in the data base')
        #return msg

    else:
        aa=False
        woeid= weather[0]['woeid']

ENDPOINT = '/api/location/{}/'.format(woeid)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None)

# -- Wait for the server's response
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Read the response's body
data1 = r1.read().decode("utf-8")

info = json.loads(data1)

time = info['time']
sunset = info['sun_set']
temp = info['consolidated_weather'][0]['the_temp']

print("In {} the ime is: {}".format(city, time))
print("The temperature in {} is {}ºC".format(city, temp))
print("The sunset in {} is at {}".format(city, sunset))






#retrievewoeid (city)