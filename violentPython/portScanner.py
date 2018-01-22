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
        connSkt.connect((tgtHost, tgtPort))
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
        print("Scanning ports" + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parser = argparse.ArgumentParser(description="specify the host and a port")
    parser.add_argument("tgtHost", help='specify target host')
    parser.add_argument("tgtPort", type=int, help='specify target port')
    args = parser.parse_args()
    print("[+] scanning host {} on port # {}".format(args.tgtHost, args.tgtPort))
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPort).split(' , ')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print("[-] You must specify a target host and port[s]")
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
