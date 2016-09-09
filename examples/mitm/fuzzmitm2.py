#!/usr/bin/python

# Note: writing MITM like this, the line
# self.server.meet(self.client)
# in MITMServer class in file network.py should be commented away


from network import *
from config import *

config = MITMConfig("mitm.cfg")

s = MITMServer(config)

while True:
    asyncore.loop(timeout=9999, count=1)

    client_request = s.client.receive(9999)
    s.server.send_data(client_request, nolog=True)

    response = s.server.receive(9999)
    f = Fuzzer([response], config.out_dir)
    s.client.send_data(f.next())
    s.client.close()
    s.server.close()
