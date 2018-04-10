#!/usr/bin/python
#
# Simplest Form Of Packet sniffer in python
# Works On Linux Platform

# import module
import socket
host = "172.26.99.17"

# create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a packet
while True:
    # print output on terminal
    print s.recvfrom(65565)
