import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except(Exception) as e:
        print(str(e))


def checkVulns(banner):
    if "(vsFTPd 2.3.4)" in banner:
        print("[+] vsFTPd FTP server vulnerable")
    elif '3COM 3CDaemon FTP Server Version 2.0' in banner:
        print("[+] 3COM 3CDaemon FTP Server vulnerable")
    else:
        print("[-] FTP Server is not vulnerable")


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(123, 128):
        ip = '172.16.133.' + str(x)
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print("[+]" + ip + ":" + banner.strip('\n'))
                checkVulns(banner)


if __name__ == '__main__':
    main()
