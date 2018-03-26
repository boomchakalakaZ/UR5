# UR5 testing connection
import socket
import time
import sys

HOST = "192.168.0.103" # The remote host
PORT = 30002 # The same port as used by the server

print ("Starting Program")

count = 0
while (count < 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(1)

    print ("Set output 1 and 2 high")

    s.send (b"set_digital_out(1,True)" + b"\n")
    time.sleep(0.1)
 
    s.send (b"set_digital_out(2,True)\n")
    time.sleep(2)



    #print ("Robot starts Moving to 3 positions based on joint positions")
    #movej([base,shoulder,elbow,wrist1,wrist2,wrist3], a is joint acceleration, v joint speed, t is time, r is blend radius) in radians
    #change from joint position to joint pose e.i x,y,z with movej(p[.....)
    #in mm e.i .43 = 430.00mm
    #s.send (b"movej([-1.80, -1.90, 1.16, -1.15, -1.55, 1.18], a=1.0, v=0.1)" + b"\n")
    #time.sleep(10)

    print("moving joints")
    s.send(b"movej([0, -1.7, 0, -1.5, 0, 0], a=1.0, v=1.0)" + b"\n")
    time.sleep(3)

    print("halting")
    s.send (b"halt" + b"\n")
    time.sleep(2)

    print("Moving position")
    s.send(b"movej(p[0.0, 0.4, 0.4, 0, 0, 1], a=1.0, v=.5)" + b"\n")
    time.sleep(5)

    count = count + 1
    print ("The count is: ", count)

    print ("Program finish")

    time.sleep(1)
    #data = s.recv(1024)

    s.close()
    #print ("Received", repr(data))

print ("Status data received from robot")

#---------------------------------------------------------------------------------------------------