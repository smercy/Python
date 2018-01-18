"""
Created on Jan 17th 2018

@author: smercy
"""

import crypt


def testPass(cryptPass):
    #  salt = cryptPass[0:11]
    #  print(salt)
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, cryptPass)
        print(cryptWord)
        if(cryptWord == cryptPass):
            print("[+] Found Password: " + word + "\n")
            return
    print("[-] Password Not Found.\n")
    return


def main():
    passFile = open('shadow.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password for: " + user)
            testPass(cryptPass)


if __name__ == '__main__':
    main()
