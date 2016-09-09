#!/usr/bin/python
from network import *
from config import *

config = ServerConfig("server.cfg")

s = Server(config)

while True:
        
    s.wait_for_connection()
        
    client_request=s.client.receive(2)
    if client_request is Timeout:
        print "Timeout waiting for data, disconnecting\n"
        s.client.close()
        break
    else:
        print "Message received from client:\n\n", client_request, "\n"		
        s.client.send_data("OK, Message received",nolog=True)
        s.client.close()

