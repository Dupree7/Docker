from scapy.all import ARP, Ether, srp

eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = "198.13.13.0/16")
answered, unanswered = srp(eth / arp, timeout = 1)
for it in answered:
    print it[1].psrc, " -- ", it[1].hwsrc

