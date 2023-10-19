from socket import *
from random import randint

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

while True:
    rand = randint(0, 10)
    message, addr = serverSocket.recvfrom(1024)
    message = message.decode().upper()
    if rand < 4:
        continue
    serverSocket.sendto(message.encode(), addr)