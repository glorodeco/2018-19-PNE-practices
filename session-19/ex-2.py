import http.client
import json

# -- API information


def retrievewoeid (city):

    try:
        HOSTNAME = "www.metaweather.com"

        ENDPOINT = "/api/location//search/?query"
        ENDPOINT += city
        METHOD = "GET"


        # -- Here we can define special headers if needed
        headers = {'User-Agent': 'http-client'}

        # -- Connect to the server
        # -- NOTICE it is an HTTPS connection!
        conn = http.client.HTTPSConnection(HOSTNAME)

        # -- Send the request. No body (None)
        # -- Use the defined headers
        conn.request(METHOD, ENDPOINT, None, headers)

        # -- Wait for the server's response

        r2 = conn.getresponse()

        # -- Print the status
        print()
        print("Response received: ", end='')
        print(r2.status, r2.reason)

        # -- Read the response's body and close
        # -- the connection
        text_json = r2.read().decode("utf-8")
        conn.close()

        # -- Optionally you can print the
        # -- received json file for testing
        # print(text_json)

        # -- Generate the object from the json file
        weather = json.loads(text_json)

        return weather[0]['woeid']

    except:

        return False

HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location//search/?query"


city= input('Your city: ')

if not (retrievewoeid(city)):
    print('Your city is not important for me')

else:
    LOCATION_WOEID = str(retrievewoeid(city))
    METHOD = 'GET'

    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standar one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)

    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

    # -- Wait for the server's response
    r2 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r2.status, r2.reason)

    # -- Read the response's body and close
    # -- the connection
    text_json = r2.read().decode("utf-8")
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    weather = json.loads(text_json)

    # -- Get the data
    time = weather['time']
    temp0 = weather['consolidated_weather'][0]
    description = temp0['weather_state_name']
    temp = temp0['the_temp']
    place = weather['title']

    print()
    print("Place: {}".format(place))
    print("Time: {}".format(time))
    print("Weather description: {}".format(description))
    print("Temperature: {} degrees".format(temp))


