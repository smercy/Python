# Networking

import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("172.166.133.127", 21))
ans = s.recv(1024)
print(ans)
