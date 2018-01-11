# Networking

import socket
socket.setdefaulttimeout(30)
s = socket.socket()
# connect() takes exactly one argument
# used inner bracket to combine add and port into one argument

s.connect(("172.16.133.164", 21))
ans = s.recv(1024)
print(ans)
