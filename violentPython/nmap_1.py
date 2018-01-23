"""
Created on Jan 22nd 2018

@author: smercy
"""

import argparse
import nmap
from threading import *
screenLock = Semaphore(value=1)


def nmapScan(tgtHost, tgtPort):
    nm = nmap.PortScanner()
    nm.scan(tgtHost, tgtPort)
    type(tgtPort)
    portstatus = nm[tgtHost]['tcp'][int(tgtPort)]['state']
    screenLock.acquire()
    print("[*] {} tcp port {} is {}".format(tgtHost, tgtPort, portstatus))
    screenLock.release()
    nmapScan.close()
    

def main():
    parser = argparse.ArgumentParser('usage%prog')
    parser.add_argument("tgtHost")
    parser.add_argument("tgtPort")
    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPort = args.tgtPort
    tgtPorts = str(tgtPort).split(',')
    print("Arguments test 1: " + tgtHost, tgtPort)
    if(tgtHost is None) | (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)
    # setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=nmapScan, args=(tgtHost, tgtPort))
        t.start()
        # print(tgtPort)
        # nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
