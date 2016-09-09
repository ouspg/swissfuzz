#!/usr/bin/python
from network import *
from config import *


config=ServerConfig("httpserver.cfg")

response = RawFile("response")
input = open_input(config.input,config)

if config.fuzz:
    input = Fuzzer(input,config.out_dir)

s=Server(config)

while True:
    s.wait_for_connection()
    p=s.client.receive(2)
    if p is Timeout:
      print "Timeout"
    else:
      s.client.send_data(response[0])
      s.client.send_data(input.next())
    s.client.close()


