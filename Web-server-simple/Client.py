from socket import *

serverName = '127.0.0.1'
serverPort = 3000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
outputData = 'GET /hello-world.html HTTP/1.0\r\nHost: 127.0.0.1\r\n\r\n'
clientSocket.send(outputData.encode())

data = 1
while data:
    data = clientSocket.recv(1024)
    print(data.decode(), end = '')
clientSocket.close()