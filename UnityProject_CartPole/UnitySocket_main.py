import socket
import time
import numpy as np
import sys

dt = 0.01
g = 9.81
l = 2.5
m1 = 50
m2 = 20
p_k = np.pi/2
pd_k = 0
pdd_k = 0
x_k = 0
xd_k = 0
xdd_k = 0
p = np.pi/2
pd = 0
pdd = 0
x = 0
xd = 0
xdd = 0


# https://stackoverflow.com/questions/53933981/lossless-movement-in-hinge-joints-unity

host = "127.0.0.1"  # localhost ip
port_pole = 25003  # Using a random open port
port_cart = 25002  # Using a random open port

# AF_INET is the address family IPV4
unitySocket_pole = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
unitySocket_cart = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connecting to Unity C# socket script

# transformRotation = [0, 0, 0]
# transformPosition = [0, 0, 0]
# positionString = ','.join(map(str, transformPosition))  # Converting Vector3 to a string,
# rotationString = ','.join(map(str, transformRotation))  # Converting Vector3 to a string,
# fullString = positionString + ',' + rotationString
# print(fullString)
# print(rotationString)
# print(transformRotation)
# exit()

unitySocket_pole.connect((host, port_pole))
unitySocket_cart.connect((host, port_cart))

# try:
# unitySocket.connect((host, port))
# except:
#     print("\nCould not connect to IPV4:", host, "Port:", port)
# unitySocket.connect(host, port)
# finally:
#     # TODO add error code

transformPosition_cart = [0, 0, 0]  # [X, Y, Z]
transformRotation_cart = [0, 0, 0]  # [roll, pitch, yaw]

transformPosition_pole = [0, 0, 0]  # [X, Y, Z]
transformRotation_pole = [0, 0, 0]  # [roll, pitch, yaw]

count = 0
running = True
# exit()
t_time = 0
f = 0.5
w = 2 * np.pi * f

while running:
    # pdd = (-g * np.sin(p)) / l
    xdd = (-m2 * l * pdd * np.cos(p) + m2 * l * pd ** 2 * np.sin(p))/(m1+m2)
    pdd = (-g * np.sin(p) - xdd * np.cos(p)) / l

    pd_k = pd + dt*pdd
    pd = pd_k

    xd_k = xd + dt*xdd
    xd = xd_k

    p_k = p + dt*pd
    p = p_k

    x_k = x + dt*xd
    x = x_k

    # TODO create check that packages have been successfully received
    time.sleep(0.01)
    transformPosition_cart[0] = x
    transformPosition_pole[0] = x
    transformRotation_pole[2] = p*180/np.pi

    positionString_cart = ','.join(map(str, transformPosition_cart))  # Converting Vector3 to a string,
    positionString_pole = ','.join(map(str, transformPosition_pole))  # Converting Vector3 to a string,
    rotationString_cart = ','.join(map(str, transformRotation_cart))  # Converting Vector3 to a string,
    rotationString_pole = ','.join(map(str, transformRotation_pole))  # Converting Vector3 to a string,
    fullString_cart = positionString_cart + ',' + rotationString_cart
    fullString_pole = positionString_pole + ',' + rotationString_pole
    # for example, transformRotation is converted from [0, 0, 0] to "0, 0, 0"
    if count % 1000 == 0:
        # print(fullString_cart)
        print("X:", transformPosition_cart, "P:", transformRotation_pole)

    unitySocket_pole.sendall(fullString_pole.encode("UTF-8"))  # Converting string to Bytes in UTF-8 format,
    unitySocket_cart.sendall(fullString_cart.encode("UTF-8"))  # Converting string to Bytes in UTF-8 format,
    # and sends it to C# script
    receivedData_pole = unitySocket_pole.recv(1024).decode("UTF-8")
    receivedData_cart = unitySocket_cart.recv(1024).decode("UTF-8")
    if count % 1000 == 0:
        print(receivedData_pole, "------", receivedData_cart)
    count += 1
    t_time += 0.01

