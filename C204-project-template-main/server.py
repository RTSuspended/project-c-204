
import socket
from  threading import Thread

SERVER = None
PORT = '127.0.0.1'
IP_ADDRESS = 6000

CLIENTS = {}

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** TAMBOLA GAME ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")


setup()
