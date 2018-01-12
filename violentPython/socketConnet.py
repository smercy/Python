"""
Created on Thursday, Jan 11th 2018
@author: smercy
"""

# Networking

import socket
socket.setdefaulttimeout(30)
s = socket.socket()
# connect() takes exactly one argument
# used inner bracket to combine add and port into one argument

s.connect(("172.16.133.124", 21))   # ip of metasploitable
ans = str(s.recv(1024))

# results
# Stephens-MBP:violentPython stephenmercy$ python3 socketConnet.py
# b'220 (vsFTPd 2.3.4)\r\n'

if("(vsFTPd 2.3.4)" in ans):
    print("[+] vsFTPd is vulnerable")
elif("Ability Server 2.34 in" in ans):
    print("[+]Ability FTP Server vulnerable")
else:
    print("[-]FTP Server is not vulnerable")

# Stephens-MBP:violentPython stephenmercy$ python3 socketConnet.py
# b'220 (vsFTPd 2.3.4)\r\n'
# [+] vsFTPd is vulnerable
