"""
Created on Jan 19th 2018

@author: smercy
"""

import argparse
import socket
from socket import *


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, int(tgtPort)))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(1000)
        print("[+]{}tcp open".format(tgtPort))
        print("[+]" + str(results))
        connSkt.close()
    except Exception:
        print("[-]{}tcp closed".format(tgtPort))


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except Exception:
        print("[+] Cannot resolve {}: Unknown host".format(tgtHost))
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("'\n'[+] Scan results for: " + tgtName[0])
    except Exception:
        print("\n[+] Scan results for:" + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        connScan(tgtHost, tgtPort)


def main():
    parser = argparse.ArgumentParser(description="specify the host and a port")
    parser.add_argument("-H", dest="tgtHost", help='specify target host')
    parser.add_argument("-p", dest='tgtPort', help='specify target port')
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = args.tgtPort.split(',')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print("[-] You must specify a target host and port[s]")
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
