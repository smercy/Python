portlist = [21, 22, 25, 80, 443]

for x in range(1, 10):
    for ports in portlist:
        print("192.168.4." + str(x) + ":" + str(ports))
