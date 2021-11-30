"""

#
# File      :Q_4_Ports.py
# Created   : 27/11/2021 20:53
# Author    : Zoltan Takacs
# Version   : v1.0.0
# Licensing : (C) 2021 Zoltan Takacs, LYIT
#             Available under GNU Public License (GPL)
# Description: Port Scanning for the well known port range.
#
"""
if __name__ == '__main__':
    '''
  Main method of application:

  Parameters: None

  Returns: Open ports - within the pre-defined range - with names after scanning the OOPR VM.
    '''

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    subprocess.call("cls", shell=True)  # Clearing the screen


# Asking for host IP we want to scan
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Status
print("=" * 50)
print(" " * 5 + "Scan in progress on host", remoteServerIP)
print("=" * 50)

# Current system time
t1 = datetime.now()

try:

    for port in range(0, 81):  # The value is determining the port range will be scanned.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))

        # Defining which port name belongs to which port number.
        if port == 22:
            print("SSH port:{} is open".format(port))
        elif port == 80:
            print("HTTP port:{} is open".format(port))
    sock.close()

# Error handling.
except KeyboardInterrupt:
    print("Process is interrupted.")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the system time again.
t2 = datetime.now()

# Calculates how long the task took to execute.
total = t2 - t1

# Printing the time
print('Scanning Completed in: ', total)

if __name__ == "__main__":
    port_scan()
