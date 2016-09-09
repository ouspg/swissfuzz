#!/usr/bin/python
from network import *
from config import *

config = ServerConfig("server.cfg")

f = open_input(config.input, config)

if config.fuzz:
    f = Fuzzer(f, config.out_dir)

s = Server(config)


while True:

    s.wait_for_connection()

    client_request = s.client.receive(2)
    if client_request is Timeout:
        print "Timeout waiting for data, disconnecting\n"
        s.client.close()
        break
    else:
        print "Message received from client:\n"
        print client_request
        print "\n"

    case = f.next()
    s.client.send_data(case, ppid=config.ppid)
    s.client.close()
