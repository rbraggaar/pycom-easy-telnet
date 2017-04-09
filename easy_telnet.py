"""
Easy telnet client for Pycom.

Fire up a telnet connection between your pc and Lopy/Wipy with a simple
script.

No need to install additional programs (besides Python itself).
"""
import telnetlib
import time
import sys
import msvcrt


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
tel.write(password + "\r\n")
print tel.read_until(">>> ", timeout=TO).strip('>>> ')

# receive commands from the user as input
# send and execute commands to the pycom device and return the result
while True:
    indent = '    '
    cmd = raw_input('>>> ')
    if len(cmd) > 1:
        while cmd[-1] == ':':
            cmd += '\n' + indent + raw_input('... ' + indent)
            indent += '    '
    tel.write(cmd + '\r\n')
    print (tel.read_until(">>> ", timeout=1).strip('>>> ' + cmd).strip('\r\n'))
