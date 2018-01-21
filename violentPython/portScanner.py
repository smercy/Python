"""
Created on Jan 19th 2018

@author: smercy
"""

import optparse
import socket
from socket import *


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(1000)
        print("[+]%d/tcp open" % tgtPort)
        print("[+]" + str(results))
        connSkt.close()
    except Exception:
        print("[-]%d/tcp closed" % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except Exception:
        print("[+] Cannot resolve '%s' : Unknown host" % tgtHost)
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
    parser = optparse.OptionParser('usage%prog -H <host> -p <port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify host')
    parser.add_option('-p', dest='tgtPort', type='int', help='specify port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(' , ')
    if (tgtHost is None) | (tgtPorts[0] is None):
        print("[-] You must specify a target host and port[s]")
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
