import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image

SERVER = None
PORT = 6000
IP_ADDRESS = '127.0.0.1'


def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow  = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.attributes('800x600')


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/4.5, screen_height/8, text = "Enter Name", font=("Chalkboard SE",60), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/7 - 130, y=screen_height/5.5)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def acceptConnections():
    global CLIENTS
    global SERVER

while True:
    player_socket, addr = SERVER.accept()
    player_name = player_socket.recv(1024).decode().strip()
    print(player_name)
    if(len(CLIENTS.keys()) == 0):
        CLIENTS [player_name] = {'player_type': 'player1'}
    else:
        CLIENTS [player_name] = {'player_type: "player2'}

    CLIENTS [player_name]["player_socket"] = player_socket
    CLIENTS [player_name]["address"] = addr
    CLIENTS [player_name]["player_name"] = player_name
    CLIENTS [player_name]["turn"] = False
    print (f"Connection established with {player_name} : {addr}")

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    askPlayerName()




setup()
