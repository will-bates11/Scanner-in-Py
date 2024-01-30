Port Scanner README

Overview

This Port Scanner is a Python-based tool designed for scanning open ports on a specified IP address. It employs multi-threading to enhance scanning speed and efficiency. The scanner is useful for network administrators, security professionals, and anyone interested in evaluating network security or performing diagnostics.

Features

Fast scanning using multi-threading.
Customizable port range.
User-friendly command-line interface.
Logging of open ports.
Adjustable timeout for port scanning.

Requirements

Python 3.x

Installation

Ensure Python 3.x is installed on your system.
Download the script scanner.py.
No additional libraries are required as the script uses standard Python libraries.

Usage

To use the Port Scanner, run it from the command line with the following syntax:
python scanner.py <IP> [-s START_PORT] [-e END_PORT]
<IP>: Target IP address to scan.
-s START_PORT, --start START_PORT: (Optional) Start port number (default is 1).
-e END_PORT, --end END_PORT: (Optional) End port number (default is 1024).

Example:
python scanner.py 192.168.1.1 -s 1 -e 5000
This command scans the IP 192.168.1.1 from port 1 to 5000.

Configuration

The number of threads can be modified in the main function by changing the num_threads parameter.
The timeout for each port scan can be adjusted in the scan_port function.

Logging

The script uses Python's logging module to log open ports. It is currently set to display information on the console. The logging level and format can be changed in the logging.basicConfig call in the script.

Disclaimer

Port scanning can be interpreted as a hostile action by network administrators. Always have explicit permission to scan networks and systems.

Contributing

Contributions to the Simple Port Scanner are welcome. Please ensure that your contributions adhere to best practices for security and efficiency.
