#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, port):

	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		s.connect((address, port))
		data = s.recv(1024)
		s.close()

		return data.decode("utf-8")
	except (socket.timeout, ConnectionRefusedError):
		return "connection error"


def main(argv):
	address = 'localhost'
	port = 20143 
	secret_message = get_accessible_ports(address, port)
	print(secret_message)
# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 1:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
