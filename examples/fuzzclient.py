#!/usr/bin/python

from network import *
from config import *

config = ClientConfig("client.cfg")

f = open_input(config.input, config)
if config.fuzz:
	f=Fuzzer(f, config.out_dir)

valid_msg = RawFile("samples/demo/client/sample.txt")

while True:
	c=Client(config)

	#print " -------- Send Valid request -----------\n"
	c.server.send_data(valid_msg[0],nolog=True)

	response=c.server.receive(2)
	if response is Timeout:
		print "Timeout in receiving valid case response- Possible DoS. Quitting.."
		quit()
	else:
		#print "Response for valid request\n"
		#print response
		pass
	c.server.close()
	time.sleep(1)



	case=f.next()
	c=Client(config)
        
	if config.fuzz:
        	c.server.send_data(case)
		print "FUZZING CASE",case
	else:
        	c.server.send_data(case,nolog=True)
		print "RESENDING CASE",case

	response=c.server.receive(2)
	if response is Timeout:
		#print "Timeout in receiving fuzzed case response.."
		pass
	else:
		#print "Response for fuzzed request\n"
		print response
		pass

	c.server.close()
	time.sleep(1)

#python fuzzclient.py -r --last 3        
        
