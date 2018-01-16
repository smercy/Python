"""
Created on Jan 14th 2018

@author: smercy

"""


iteration = 0
count = 0
while iteration < 1:
    for things in "hello, world":
        count += 1
        # print(count)
    print("iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# test 3
"""
count = 0
phrase = "hello, world"

for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("iteration " + str(iteration) + "; count is: " + str(count))
"""
