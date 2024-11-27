#!/usr/bin/python3

import base64
import pyshark
import argparse

DES = []

def decode(text):
	return base64.b32decode(text.encode()).decode()

def process(packet):
	try:
		if packet.dns.qry_name.split('.')[1] == args.address.split('.')[0] and packet.dns.qry_name.split('.')[0] not in DES:
			DES.append(packet.dns.qry_name.split('.')[0])
	except AttributeError: pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Packety .pcap decoder.", usage="%(prog)s -a <address>  -c <capture.pcap> -f <output file>")
	parser.add_argument("-a", "--address", help="Address to filter.", required=1, metavar='')
	parser.add_argument("-c", "--cap-file", help=".pcap file to decode.", required=1, type=argparse.FileType('r'), dest="cap", metavar='')
	parser.add_argument("-f", "--file", help="File to write", required=1, metavar='')
	args = parser.parse_args()

	print("𝔽 𝕀 𝕃 𝕋 ℝ ℤ    -   𝕊. ℝ𝕒𝕪\n")

	print("[*] Filtering...")
	cap = pyshark.FileCapture(args.cap.name, keep_packets=0)
	cap.apply_on_packets(process)

	text = ""
	for qry in DES: text += qry[1:-2]

	open(args.file, 'w').write(decode(text))
	print("[*] Saved as: " + args.file)