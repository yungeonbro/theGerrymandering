from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pygame
from ServerManager import *
import time
import gamelogic
import gameplay
import threading

manager = ServerManager('key2.json',  'https://gerrymandering-296813.firebaseio.com/')

root = Tk()

root.title("The GerryMandering Online")
root.geometry("400x120")

def wait(pwd): # wait until appointment comes up
	print('waiting for appointment')
	while(not manager.hasGameStarted(pwd)):
		time.sleep(1)
	playGame(pwd, 'dem')
	return 


def playGame(pwd, side): 
	print('you are playing as '+side)
	gameplay.playGame(side, pwd, manager)


def enterpassword():
	pwd = entry.get()
	isWaitingGame = manager.isWaitingGame(pwd) # turn started true
	if not isWaitingGame:
		slabel.config(text = 'status : waiting for appointment')
		manager.addGame(pwd)
		t = threading.Thread(target = wait, args = [pwd])
		t.start()

		
	if isWaitingGame:
		playGame(pwd, 'rep')

yd = 80
xd = 10
entry = Entry(root)
entry.place(x=150-xd, y=100-yd)

button = Button(root, text = 'enter', command = enterpassword)
button.place(x=300-xd, y=96-yd)

label = Label(root, text = 'Enter Password')
label.place(x=50-xd, y=100-yd)

slabel = Label(root, text = 'status : waiting for password')
slabel.place(x=50-xd, y=140-yd)
root.mainloop()