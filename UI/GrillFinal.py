# Echo client program
import socket
import sys
import time

HOST = "192.168.0.105" # The remote host
PORT = 30001 # The same port as used by the server

POSITIONS = [0, -0.225] # The positions supported by the algorithm

state = 0
states = []

def define(wait, pos):
    states.append([wait, pos])

def waypoint(wait, pos):
    s.send(bytes('movej('+pos+',t='+str(wait)+')\n',encoding='utf-8'))
    time.sleep(wait)
    global state
    state += 1
    print('State(' +str(state) + ')')

def defineHome():
    define(4.0,   '[1.770, -1.633, -1.694, -3.498, -1.412, 0.089]')

def toGrill(x):
    defineHome()
    define(4.0,   'p[0.468, 0.236, 0.269, 0.2316, 2.9582, 1.2507]')
    define(1.4,   'p[0.453, 0.216, 0.140, 0.0866, 2.7157, 1.4616]')
    define(0.4,   'p[0.454, 0.246, 0.134, 0.0687, 2.7030, 1.4606]')
    define(0.3,   'p[0.450, 0.252, 0.162, 0.0492, 2.6841, 1.4718]')
    define(0.6,   'p[0.449, 0.294, 0.168, 0.1975, 2.7642, 1.4172]')
    define(0.6,   'p[0.445, 0.344, 0.156, 0.1561, 2.7698, 1.3473]')
    define(0.4,   'p[0.441, 0.321, 0.176, 0.1273, 2.7384, 1.3503]')
    define(0.9,   'p[0.439, 0.332, 0.282, 0.0933, 2.7388, 1.3642]')
    define(2.5,   'p[0.029, 0.474, 0.245, 0.1432, 1.5538, 2.9345]')
    define(3.0,   'p[0.063, 0.473, 0.273, 0.0835, 2.6750, 1.5631]')

    define(1.8,   'p['    +   str(0.077+x)   +   ', 0.594, 0.292, 0.0733, 2.9256, 0.9435]')
    define(0.6,   'p['    +   str(0.076+x)   +   ', 0.584, 0.296, 0.0999, 2.9786, 0.7792]')
    define(7.0,   'p['    +   str(0.076+x)   +   ', 0.448, 0.269, 0.0750, 2.9322, 0.9120]')
    define(1.0,   'p['    +   str(0.086+x)   +   ', 0.352, 0.380, 0.0669, 2.9550, 0.8027]')

def center(x):
    defineHome()
    define(1.5,   'p['    +   str(0.092+x)   +   ', 0.400, 0.245, 0.0790, 2.9183, 1.2372]')
    define(4.0,   'p['    +   str(0.092+x)   +   ', 0.480, 0.245, 0.0783, 2.9185, 1.2374]')
    define(0.6,   'p['    +   str(0.093+x)   +   ', 0.461, 0.286, 0.1673, 2.9241, 1.1843]')
    define(4.0,   'p['    +   str(0.073+x)   +   ', 0.777, 0.403, 2.4605, -2.5736, 0.8406]')
    define(0.8,   'p['    +   str(0.074+x)   +   ', 0.777, 0.330, 2.4572, -2.5755, 0.8410]')
    define(4.0,   'p['    +   str(0.051+x)   +   ', 0.777, 0.332, 2.4572, -2.5752, 0.8414]')
    define(0.7,   'p['    +   str(0.051+x)   +   ', 0.777, 0.387, 2.4598, -2.5736, 0.8410]')
    define(2.3,   'p['    +   str(0.087+x)   +   ', 0.697, 0.538, 3.4991, -0.1465, -0.0739]')
    define(2.4,   'p['    +   str(0.087+x)   +   ', 0.758, 0.395, 2.5392, 2.4551, -0.8518]')
    define(0.7,   'p['    +   str(0.087+x)   +   ', 0.758, 0.336, 2.5417, 2.4535, -0.8515]')
    define(4.0,   'p['    +   str(0.141+x)   +   ', 0.758, 0.332, 2.5415, 2.4546, -0.8509]')
    define(0.5,   'p['    +   str(0.141+x)   +   ', 0.758, 0.370, 2.5398, 2.4557, -0.8511]')
    define(2.0,   'p['    +   str(0.086+x)   +   ', 0.646, 0.529, 0.1910, 3.1536, -0.0297]')

def offGrill(x):
    defineHome()
    define(0.9,   'p['    +   str(0.124+x)    +   ', 0.435, 0.210, 0.0051, 2.8971, 1.3433]')#
    define(0.9,   'p['    +   str(0.099+x)    +   ', 0.569, 0.190, 0.0763, 2.8210, 1.4443]')#
    define(1.0,   'p['    +   str(0.090+x)    +   ', 0.542, 0.139, 0.0135, 2.4952, 1.8528]')
    define(2.0,   'p['    +   str(0.093+x)    +   ', 0.494, 0.124, 0.0533, 1.8104, 2.5605]')
    define(3.0,   'p[0.395, 0.521, 0.287, 0.2429, 2.6036, 1.4494]')
    define(1.0,   'p[0.413, 0.534, 0.302, 0.0296, 2.8733, 0.7897]')
    define(1.0,   'p[0.397, 0.505, 0.390, 0.0175, 2.7617, 0.9415]')

def flip(x):
    defineHome()
    define(0.9,   'p['    +   str(0.124+x)    +   ', 0.435, 0.210, 0.0051, 2.8971, 1.3433]')#
    define(0.9,   'p['    +   str(0.099+x)    +   ', 0.569, 0.190, 0.0763, 2.8210, 1.4443]')#
    define(1.0,   'p['    +   str(0.123+x)    +   ', 0.542, 0.139, 0.0135, 2.4947, 1.8537]')
    define(2.0,   'p['    +   str(0.093+x)    +   ', 0.494, 0.124, 0.0533, 1.8104, 2.5605]')
    define(1.0,   'p[0.092, 0.521, 0.356, 0.0924, 0.9644, 3.0099]')
    define(1.0,   'p[0.064, 0.595, 0.372, 0.3578, 0.4263, 1.5575]')
    define(1.0,   'p[0.028, 0.567, 0.320, 1.9430, -1.6945, -5.4368]')
    define(1.0,   'p['    +   str(0.070+x)    +   ', 0.503, 0.219, 5.2607, -0.5322, -0.0542]')
    define(1.0,   'p['    +   str(0.075+x)    +   ', 0.486, 0.190, 4.6742, -0.1525, 0.1879]')
    define(0.5,   'p['    +   str(0.089+x)    +   ', 0.434, 0.192, 4.6345, -0.1287, 0.1921]') 
    define(0.7,   'p['    +   str(0.068+x)    +   ', 0.434, 0.290, 4.6332, -0.1240, 0.1840]')

# Sets up the positions for the program. 
def setup():   
    for position in POSITIONS:
        toGrill(position)
        center(position)

    for position in POSITIONS: 
        flip(position)
        center(position)

    for position in POSITIONS:
        offGrill(position)
   
count = 0
setup()

if len(sys.argv) >= 2: 
    state = int(sys.argv[1])

while (count < 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(0.5)

    for i in range(state, len(states)):
        x = states[i]
        waypoint(x[0], x[1])

    count = count + 1
    print("The count is:", count)
    print("Program finish")
    
    time.sleep(1)
    data = s.recv(1024)

    s.close()
    print ("Received", repr(data))


print("Status data received from robot")