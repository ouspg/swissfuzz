#!/usr/bin/python
from network import *
from config import *
from subprocess import Popen, PIPE, STDOUT

config = MITMConfig("server.cfg")

# Simple example of what MITM fuzzer could look like

class FuzzMitm(MITMServer):
  def fuzz(self, data):
    fuzzed = data
    while fuzzed == data:
      p = Popen("radamsa", stdout=PIPE, stdin=PIPE, stderr=STDOUT)
      fuzzed=p.communicate(input=data)[0]
    data = fuzzed
    return data

  def handle_connection(self):
    self.client.send_hook=self.fuzz
  
server=FuzzMitm(config)
asyncore.loop()

    

        
        
