# UR5 testing connection
import socket
import time
import sys

HOST = "192.168.0.103" # The remote host
PORT = 30002 # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(1)

# Assuming tool is on the mount, set voltage to 12 to hold the tool.
# DO NOT SET IT TO 24
s.send(b"set_tool_voltage(12)\n")
time.sleep(1)
#movej([base,shoulder,elbow,wrist1,wrist2,wrist3],
#t is time
s.send(b"movej([1.5, -1.5, 0, -1.5, 0, 0], t=4.0)\n")
time.sleep(4.2)
s.send(b"movej([0.3, -1.7, -2.0, -1.0, -1.5, 0], t=4.0)\n")
time.sleep(4.2)

print ("Program finish")

s.close()
sys.exit()

#---------------------------------------------------------------------------------------------------