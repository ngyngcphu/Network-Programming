from socket import *
from time import time

serverName = '127.0.0.1'
serverPort = 3000
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    time1 = time()
    outputData = 'Ping ' + str(i) + ' ' + str(time1)
    clientSocket.settimeout(1)
    clientSocket.sendto(outputData.encode(), (serverName, serverPort))
    try:
        modifiedMessage, addr = clientSocket.recvfrom(1024)
        timeDiff = time() - time1
        print(modifiedMessage.decode() + ' RTT: ' + str(timeDiff))
    except:
        print('lost ' + str(i))