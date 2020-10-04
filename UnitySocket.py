import socket
import time

# https://stackoverflow.com/questions/53933981/lossless-movement-in-hinge-joints-unity

host = "127.0.0.1" #localhost ip
port = 25001 # Using a random open port

# AF_INET is the address family IPV4
unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to Unity C# socket script

transformRotation = [0, 0, 0]
rotationString = ','.join(map(str, transformRotation))
print(rotationString)
print(transformRotation)

unitySocket.connect((host, port))

# try:
    # unitySocket.connect((host, port))
# except:
#     print("\nCould not connect to IPV4:", host, "Port:", port)
    # unitySocket.connect(host, port)
# finally:
#     # TODO add error code
#     exit()

transformRotation = [0, 0, 0]
count = 0
running = True
while running:
    # TODO create check that packages have been successfully received
    time.sleep(0.01)
    transformRotation[0] += 1
    rotationString = ','.join(map(str, transformRotation))  # Converting Vector3 to a string,
    # for example, transformRotation is converted from [0, 0, 0] to "0, 0, 0"
    if count % 1000 == 0:
        print(rotationString)

    unitySocket.sendall(rotationString.encode("UTF-8"))  # Converting string to Bytes in UTF-8 format,
    # and sends it to C# script
    receivedData = unitySocket.recv(1024).decode("UTF-8")
    if count % 1000 == 0:
        print(receivedData)
    count += 1
