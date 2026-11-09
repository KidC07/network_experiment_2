from socket import *
serverName = '172.26.214.63'
serverPort = 5012
clientSocket = socket(AF_INET, SOCK_DGRAM)   
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort));
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close();
