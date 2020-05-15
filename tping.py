#-*-coding: utf-8-*-
from scapy.all import *
print"""
#############################################
# Tping v.1.0 by: Renegado                  #
#############################################
"""
host = raw_input("Host> ")
pack = int(input("Package> "))
x = IP(dst=host)/TCP()
y = send(x*pack)
print y
