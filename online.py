import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pygame
from InputBox import InputBox
#database 
cred = credentials.Certificate('key.json')

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://gerrymandering-36b75.firebaseio.com/'
})

dir = db.reference();

dir.update({'games':[{'password':'123abc'}]})

print(dir.get())

pwd = input('Enter password : ')

#pygame
pygame.init()

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
GREY = (100, 100, 100)
HIGHLIGHT = (160, 217, 46)
LIGHTBLUE = (200, 200, 255)
LIGHTRED = (255, 200, 200)
LIGHTGREY = (200, 200, 200)

#font
font = pygame.font.Font(None, 25)
bigfont = pygame.font.Font(None, 80)

# Set the height and width of the screen
size  = [800,600]
width = size[0]
height = size[1]

screen= pygame.display.set_mode(size)
  
pygame.display.set_caption("the Gerrymandering")
  
#Loop until the user clicks the close button.
done= False
clock= pygame.time.Clock()

while not done:
    clock.tick(10)

    keys = pygame.key.get_pressed()

    # Main Event Loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True # Flag that we are done so we exit this loop

            screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()













