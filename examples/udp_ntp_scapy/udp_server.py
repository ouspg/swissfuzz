#!/usr/bin/python
from network import *
from config import *


config = ClientConfig("udp_server.cfg")
f = open_input(config.input, config)
if config.fuzz:
    f=Fuzzer(f, config.out_dir)

c=Client(config) # Use client even if actually server, it is just about receive first

while True:

    reply=c.server.receive(999)
    if reply is Timeout:
        print "Timeout waiting for data! Possible DoS, Quitting.."
        quit()
    else:
        print "\nResponse for fuzzed message:\n"
        print reply

    c.server.send_data(f.next())


