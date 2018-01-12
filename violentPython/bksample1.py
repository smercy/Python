# variables and type
port = 21
print(type(port))

banner = "Freefloat FTP Server "
print(type(banner))

portList = [21, 22, 80, 110]
print(type(portList))

portOpen = True
print (type(portOpen))

print ("[+] checking for "+banner + "on port" + str(port))

# page 8 string methods
print banner.upper()
print banner.lower()
print banner.replace('Freefloat', 'Ability')
print banner.find('FTP')

# lists #
# append
portList.append(443)
portList.append(25)
print portList

# sort
portList.sort()
print portList

# index of a list value
print(portList.index(80))

# remove a value
portList.remove(443)
print(portList)

# length of a list
print(len(portList))

# dictionary
# create a dictionary and populate with values
service = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}

# list all keys in a dictionary
print(service.keys())

# list the entire items in the dictionary
print(service.items())

# check whether a key is contained in the dictionary
print('ftp' in service)

# find the value of a specific key
print(service['ftp'])
