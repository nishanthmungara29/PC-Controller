import time
import socket
#provides acess to variables and fns for interacting with python interpreter
import sys
import os

# Initialize soc to socket
soc = socket.socket()

# Initialize the host i.e. server
host = "127.0.0.1"

# Initialize the port
port = 8080

# bind the socket with port and host
# connects client to server 
soc.connect((host, port))
print("Connected to Server.")

# receive the command from server program
#receive command from socket soc and max of 1024 bytes can be received
command = soc.recv(1024)
#convert data from bytes to string format
command = command.decode()

# match the command and execute it on client system
if command == "open":
    print("Command is :", command)
    soc.send("Command received".encode())

    #give the file name as input
    #executes batch file on client
    os.system('test.bat')