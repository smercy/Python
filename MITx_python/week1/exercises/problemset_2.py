"""
Created on Jan 14th 2018

@author: smercy

"""


string = 'azcbobobobghaklbobob'
sub = "bob"
count = 0

strlen = len(string)
sublen = len(sub)

for i in range(0, strlen):
    if string[i:i+(sublen)] == sub:
        count += 1

print("Number of times bob occurs is: " + str(count))
