import socket
import time
import numpy as np

# https://stackoverflow.com/questions/53933981/lossless-movement-in-hinge-joints-unity

host = "127.0.0.1" #localhost ip
port = 25001 # Using a random open port

# AF_INET is the address family IPV4
unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to Unity C# socket script

transformRotation = [0, 0, 0]
transformPosition = [0, 0, 0]
positionString = ','.join(map(str, transformPosition))  # Converting Vector3 to a string,
rotationString = ','.join(map(str, transformRotation))  # Converting Vector3 to a string,
fullString = positionString + ',' + rotationString
print(fullString)
print(rotationString)
print(transformRotation)
# exit()

unitySocket.connect((host, port))

# try:
    # unitySocket.connect((host, port))
# except:
#     print("\nCould not connect to IPV4:", host, "Port:", port)
    # unitySocket.connect(host, port)
# finally:
#     # TODO add error code


transformPosition = [3, 0, 0]  # [X, Y, Z]
transformRotation = [0, 0, 0]  # [roll, pitch, yaw]

count = 0
running = True
# exit()
t_time = 0
f = 0.5
w = 2*np.pi*f
while running:
    # TODO create check that packages have been successfully received
    time.sleep(0.01)
    transformRotation[0] += 1
    transformPosition[0] = 3 + 1.5*np.sin(w*t_time)
    transformPosition[1] = 1.5*np.sin(w*t_time)
    transformPosition[2] = 1.5*np.sin(w*t_time)

    positionString = ','.join(map(str, transformPosition))  # Converting Vector3 to a string,
    rotationString = ','.join(map(str, transformRotation))  # Converting Vector3 to a string,
    fullString = positionString + ',' + rotationString
    # for example, transformRotation is converted from [0, 0, 0] to "0, 0, 0"
    if count % 1000 == 0:
        print(fullString)

    unitySocket.sendall(fullString.encode("UTF-8"))  # Converting string to Bytes in UTF-8 format,
    # and sends it to C# script
    receivedData = unitySocket.recv(1024).decode("UTF-8")
    if count % 1000 == 0:
        print(receivedData)
    count += 1
    t_time += 0.01