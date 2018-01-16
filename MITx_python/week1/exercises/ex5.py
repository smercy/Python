"""
Created on Thursday, Jan 12th 2018

@author: smercy

"""

print("ex5 : 1")

num = 10

for num in range(5):
    print num
print(num)


print("ex5 : 2")

div = 2

for num in range(0, 10, 2):
    print(num/div)

print("ex5 : 3")

for var in range(20):
    if var % 4 == 0:
        print(var)
    if var % 16 == 0:
        print("foo!")



print("ex5 : 5")

count = 0

for letter in 'Snow!':
    print("Letter # " + str(count) + " is " + str(letter))
    count += 1
    break
print(count)
