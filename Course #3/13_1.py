# Name: Miller Quintero
# Date: Dec 5, 2024
# Brief: First XML parsing

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

''' This special function build the tree with XML data,
it could blows up due to an erro in the XML, something
like a slash or ar not closed tag '''
try:
    tree = ET.fromstring(data)
except:
    print("Error, bad XML.")

# Here, we used the .find method of this object, an get text
print('Name:', tree.find('name').text)
print('Name:', tree.find('phone').text.strip())
# Similar, but we get the 'hide' atributte value
print('Attr:', tree.find('email').get('hide'))