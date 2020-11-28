import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pygame
from ServerManager import *
import time
import gamelogic
import gameplay

def wait(pwd): # wait until appointment comes up
    print('waiting for appointment')
    while(not manager.hasGameStarted(pwd)):
        time.sleep(1)
    return


def playGame(pwd, side): 
    print('you are playing as '+side)
    gameplay.playGame(side, pwd, manager)


pwd = input('Enter password : ')
isWaitingGame = False

manager = ServerManager('key2.json',  'https://gerrymandering-296813.firebaseio.com/')

isWaitingGame = manager.isWaitingGame(pwd) # turn started true

if not isWaitingGame:
    manager.addGame(pwd)
    wait(pwd)
    playGame(pwd, 'dem')
if isWaitingGame:
    playGame(pwd, 'rep')

