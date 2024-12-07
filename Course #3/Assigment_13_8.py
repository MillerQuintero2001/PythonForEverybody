# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: Assigment related with scrapping data from an API

import urllib.request, urllib.parse
import ssl, json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    place = input('Enter location: ')
    if len(place) < 1: break

    # Creating query URL
    parameterQ = {'q': place}
    query_url = serviceurl + urllib.parse.urlencode(parameterQ)

    # Getting data and decode it
    print('Retrieving:', query_url)
    rawData = urllib.request.urlopen(query_url, context=ctx).read().decode()
    print(f'Retrieved {len(rawData)} characters.')

    # Parse raw data
    try:
        jsonData = json.loads(rawData)
    except:
        jsonData = None

    if not jsonData or 'features' not in jsonData:
        print('==== Download error ===')
        print(rawData)
        break

    if len(jsonData['features']) == 0:
        print('==== Object not found ====')
        print(rawData)
        break

    # This line was only for debugging
    #print(json.dumps(jsonData['features'][0]['properties'], indent=4))

    print(jsonData['features'][0]['properties']['plus_code'])