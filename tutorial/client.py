#!/usr/bin/python
from network import *
from config import *

config = ClientConfig("client.cfg")

f = open_input(config.input, config)
if config.fuzz:
    f=Fuzzer(f, config.out_dir)

while True:
    c=Client(config)

    c.server.send_data(f.next())

    reply=c.server.receive(2)
    if reply is Timeout:
        print "Timeout waiting for data! Possible DoS, Quitting.."
        quit()
    else:
        print "\nResponse for fuzzed message:\n"
        print reply

    c.server.close()
    time.sleep(0.5)



