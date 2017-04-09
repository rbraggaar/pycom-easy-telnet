"""
Easy telnet client for Pycom.

Fire up a telnet connection between your pc and Lopy/Wipy with a simple
script.

No need to install additional programs (besides Python itself).
"""
import telnetlib
import time
import sys


__author__ = "Rob Braggaar"
__license__ = "CC-BY-SA"

sys.ps1 = ''
sys.ps2 = ''
# timeout value for blocking operations [s]
TO = 5 

# host, 192.168.4.1 by default
host = "192.168.4.1"

# username and password for telnet
username = "micro"
password = "python"

# create telnet object
tel = telnetlib.Telnet(host, port=23, timeout=TO)

# login process
print tel.read_until("Login as: ")
print username
tel.write(username + "\r\n")
print tel.read_until("Password: ", timeout=TO)
print ''
time.sleep(0.5)
tel.write(password + "\r\n")
print tel.read_until(">>> ", timeout=TO).strip('>>> ')
time.sleep(0.5)

# receive commands from the user as input
# send and execute commands to the pycom device and return the result
while True:
    cmd = raw_input('>>> ')
    tel.write(cmd + '\r\n')
    time.sleep(0.2)
    print (tel.read_until(">>> ", timeout=TO).strip('>>> ' + cmd).strip('\r\n'))



