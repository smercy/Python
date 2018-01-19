
"""
Created on Jan 19th 2018

@author: smercy
"""

import zipfile
from threading import Thread
import optparse


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("[+] Found password " + password + '\n')
    except Exception:
        pass


def main():
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip')
    parser.add_option('-d', dest='dname', type='string', help='specify dict')
    (options, args) = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
