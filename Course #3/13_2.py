# Name: Miller Quintero
# Date: Dec 5, 2024
# Brief: Parsing an XML with multiple nested tags

import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

''' This special function build the tree with XML data,
it could blows up due to an erro in the XML, something
like a slash or ar not closed tag '''
try:
    stuff = ET.fromstring(input)
    # Here, with findall method is possible to specify a tag and his tags beneath 
    lst = stuff.findall('users/user')
    print('User count:', len(lst))

    # Now, iterate through every list element, that is also another xml.etree.ElementTree.Element
    for item in lst:
        # Get the nest inside 'name' tag, 'id tag, and the attribute value of key X.
        print('Name', item.find('name').text)
        print('Id', item.find('id').text)
        print('Attribute', item.get('x'))
        print('Name:', stuff.find('id').text)
except:
    print("Error, bad XML.")

