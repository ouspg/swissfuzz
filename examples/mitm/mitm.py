#!/usr/bin/python
from network import *
from config import *

config = MITMConfig("mitm.cfg")


# Listen address, bind address for outgoing connections, destination (or
# "transparent")
server = MITMServer(config)

asyncore.loop()
