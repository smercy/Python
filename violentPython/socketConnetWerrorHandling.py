"""
Created on Thursday, Jan 11th 2018
@author: smercy
"""
# Networking

import socket
socket.setdefaulttimeout(2)
s = socket.socket()
# connect() takes exactly one argument
# used inner bracket to combine add and port into one argument

try:
    s.connect(("172.16.133.124", 21))   # ip of metasploitable
except(Exception) as e:
    print("[-] Error = " + str(e))

print(s.recv(1024))


# b'220 (vsFTPd 2.3.4)\r\n'
