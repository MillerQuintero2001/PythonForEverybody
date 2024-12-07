# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: Scrapping data from an API

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Most common test wit it, is 'Ann Arbor, MI'
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    # Create simple dictionary key-value pair with the query
    parms['q'] = address
    # Now, we use .urlencode method, that receives dictionary and encoded it to do a query
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving:', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break
    # This line here, allow us to see original JSON data
    # print(json.dumps(js, indent=4))
    # print(json.dumps(js['features'], indent=4))
    # print(json.dumps(js['features'][0], indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)




