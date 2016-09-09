#!/usr/bin/python

from network import *
from config import *
from scapy.all import *

config = ClientConfig("ntp-client-scapy.cfg")

# NTP() class imported from scapy
ntp1 = NTP()
ntp1.version = 4

ntp2 = NTP()
ntp2.stratum = 3

c = Client(config)

if config.fuzz:
    f = Fuzzer([str(ntp1), str(ntp2)])
else:
    # resend from log file
    f = open_input(config.input, config)

while True:
    if config.fuzz:
        c.server.send_data(f.next())
    else:
        c.server.send_data(f.next(), nolog=True)

    time.sleep(2)
