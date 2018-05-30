# UDP client
import socket
import logging
import sys


logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.001)

sendAdr = ('172.111.0.14', 10000)

maxN = 10000
wSize = 5
viz = [0] * (maxN + wSize + 1)
left = 1
window = range(left, wSize + 1)

ok = True

while left <= maxN:
    for num in window:
        if(not viz[num] and num <= maxN):
            sock.sendto(str(num), sendAdr)
            
    for i in range(0,wSize):
        try:
            data, recvAdr = sock.recvfrom(1024)
            if(not viz[int(data)]):
                viz[int(data)] = 1
                print data
        except socket.timeout:
            break
    while viz[window[0]]:
        window = window[1:] + [left + wSize]
        left+=1

for i in range(1, maxN):
    if(not viz[i]):
        print i

sock.close()
