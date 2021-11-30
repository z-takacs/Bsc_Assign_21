"""

#
# File      :Q_3_SSH.py
# Created   : 24/11/2021 00:50
# Author    : Zoltan Takacs
# Version   : v1.0.0
# Licensing : (C) 2021 Zoltan Takacs, LYIT
#             Available under GNU Public License (GPL)
# Desription: Connecting from host PC to OOPR VM in VMware WS with SSH through a Python script.
#
"""
if __name__ == '__main__':

    '''
  Main method of application:

  Parameters: None

  Returns: Returns result of connection test.

    '''
import paramiko
import time
import re

# Open SSH connection to the device


def ssh_connection(ip):
    try:
        username = "l00169723"  # In an automation script read data from file
        password = "XXXXXXXXX"  # PW is masked

        print("Establishing a connection...")
        session = SSHClient = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("ls > dir_contents.txt\n")  # Unix command to list  directory contents and save to file
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}".format(ip))
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection("192.168.136.128")  # The IP address of VM OOPR.