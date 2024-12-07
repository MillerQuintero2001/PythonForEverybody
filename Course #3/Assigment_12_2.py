# Name: Miller Quintero
# Date: Dec 3, 2024
# Brief: Assigment about getting HTTP headers from a web page

import socket

# First, create a socket, with  the following atributes
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the specified host and its port
mysock.connect(('data.pr4e.org', 80))
# Request command, that should be enconded because originally are unicode and must be UTF-8 
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # Take 512 characters
    data = mysock.recv(512)
    # Where there is no more data to scrap, end routine
    if (len(data) < 1):
        break
    """ Decode from UTF-8 to unicode again, and print the received stream,
    using '' as the terminator, not a newline, because not all the data 
    in the stream may have arrived."""
    print(data.decode(), end='')
# Finally close the socket when there is no more data to recive
mysock.close()