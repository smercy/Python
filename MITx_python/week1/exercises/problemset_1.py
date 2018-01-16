"""
Created on Jan 14th 2018

@author: smercy

"""


s = "azcbobobegghakl"
totalvowel = 0

for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' \
            or vowel == 'u':
            totalvowel += 1
print("Number of vowels: " + str(totalvowel))
