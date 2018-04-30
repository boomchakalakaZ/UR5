# Stop robot program
# Note that robot will still run its last instruction
import socket
import time
import sys

HOST = "192.168.0.103" # The remote host
PORT = 30002 # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(1)

print("Stop")
s.send (b"stopj(.5)\n")
time.sleep(2)

s.close()
sys.exit()

#---------------------------------------------------------------------------------------------------