"""
Created on Jan 11th 2018

@author: smercy
"""

import socket
import os
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except(Exception) as e:
        print(str(e))


def checkVulns(banner, file):
    f = open(file, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("[+] Server is vulnerable: " + banner.strip('\n'))
        else:
            print("[-] FTP Server is not vulnerable")
        return


def main():
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
        if not os.path.isfile(fileName):
            print("[-] " + fileName + "Does not exist")
            exit(0)
        if not os.access(fileName, os.R_OK):
            print("[-] " + fileName + "Access denied")
            exit(0)
    else:
        print("[-] Usage: " + str(sys.argv[0]) + "<vulnerabilies fileName>")
        exit(0)

    port = 22
    ip = '192.168.2.5'
    banner = retBanner(ip, port)
    if banner:
        print("[+]" + ip + ":" + banner.strip('\n'))
        checkVulns(banner, fileName)

if __name__ == '__main__':
    main()
