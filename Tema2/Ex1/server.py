# UDP Server
import socket
import logging

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = ('0.0.0.0')
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portnul portul %d", adresa, port)

while True:
    data, address = sock.recvfrom(1024)
    if data:
        sent = sock.sendto(data, address)

sock.close()