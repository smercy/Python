"""
Created on Jan 22nd 2018

@author: smercy
"""

import argparse
import nmap


def nmapScan(tgtHost, tgtPort):
    # print(tgtHost, tgtPort)
    nmScan = nmap.PortScanner()
    print(tgtHost, tgtPort)
    nmScan.scan(tgtHost, tgtPort)
    results = nmScan[tgtHost]['tcp'][21]['state']
    print("[*] {} tcp {} {}".format(tgtHost, tgtPort, results))


def main():
    parser = argparse.ArgumentParser('usage%prog')
    parser.add_argument("tgtHost")
    parser.add_argument("tgtPort")
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPort = args.tgtPort
    tgtPorts = str(tgtPort).split(', ')
    print("Arguments test 1: " + tgtHost, tgtPort)
    if(tgtHost is None) | (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        print(tgtHost)
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
