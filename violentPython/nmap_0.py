"""
Created on Jan 22nd 2018
@author: smercy
"""

import argparse
import nmap


def nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    nm.scan(tgtHost, tgtPort)
    portstatus = nm[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*] {} tcp port {} is {}".format(tgtHost, tgtPort, portstatus))


def main():
    parser = argparse.ArgumentParser('usage%prog')
    parser.add_argument("tgtHost")
    parser.add_argument("tgtPort")
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPort = args.tgtPort
    tgtPorts = str(tgtPort).split(',')
    if(tgtHost is None) | (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
