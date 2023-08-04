"""
The project enables the server to send commands to the client, and the client executes those commands if the command received is "open".
"""

import time
import socket
import sys
import os

# Initialize soc to socket
soc = socket.socket()

# Initialize the host variable with name of local machine using gethost
host = socket.gethostname()

# Initialize the port
port = 8080

# Bind the socket with port and host
#binding to all available n/w interfaces on local machine
soc.bind(('', port))

print("waiting for connections...")

# listening for connections
soc.listen()

# accepting the incoming connections
#returns new socket obj called conn and ip addr of client and port no.
conn, addr = soc.accept()

print(addr, "is connected to server")

# take command as input
# prompting server operator to enter a command to send it to client for execution
command = input(str("Enter Command :"))

conn.send(command.encode())

print("Command has been sent successfully.")

# receive the confirmation
data = conn.recv(1024)

if data:
   print("command received and executed successfully.")