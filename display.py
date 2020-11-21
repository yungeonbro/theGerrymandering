import pygame
import main

sizeofgame = 6
game = main.Game(sizeofgame)
pygame.init()
#info of game
whoseturn = 1#dem
clicked = []

#Define the colors we will use in RGB format
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

#game size etc
outerradius = 250

blockwidth = int(outerradius/sizeofgame)
screen= pygame.display.set_mode(size)
  
pygame.display.set_caption("the Gerrymandering")
  
#Loop until the user clicks the close button.
done= False
clock= pygame.time.Clock()


while not done:
    clock.tick(10)

    # Main Event Loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            np = [pos[0], pos[1]]
            np[0] -= width/2-outerradius
            np[1] -= height/2-outerradius
            np[0] = int(np[0])
            np[1] = int(np[1])
            np[0] = int(np[0]/blockwidth)
            np[1] = int(np[1]/blockwidth)
            if np not in clicked:
                if len(clicked)<5:
                    if np[0]<sizeofgame*2 and np[0]>=0 and np[1]<sizeofgame*2 and np[0]>=0:
                        clicked.append(np)
            else:
                clicked.remove(np)

            if width/2+10<=pos[0] and pos[0]<=width/2+10+outerradius-20 and  height/2+outerradius+10<=pos[1] and pos[1]<= height/2+outerradius+10+height/2 - outerradius - 20:#gerrymanderbutton
                
                res = game.removeVoters(clicked)
                if res == 0:
                    clicked = []#make empty
                    if whoseturn == 0:
                        whoseturn = 1
                    else:
                        whoseturn = 0

            if width/2-10>=pos[0] and pos[0]>width/2+10-outerradius+20 and  height/2+outerradius+10<=pos[1] and pos[1]<= height/2+outerradius+10+height/2 - outerradius - 20:#gerrymanderbutton
                print("sdf")
    
    screen.fill(WHITE)
    if whoseturn  == 1:
        pygame.draw.rect(screen, LIGHTBLUE, [0, 0, width/2, height])
        pygame.draw.rect(screen, LIGHTGREY, [width/2, 0, width/2, height])
    if whoseturn  == 0:
        pygame.draw.rect(screen, LIGHTGREY, [0, 0, width/2, height])
        pygame.draw.rect(screen, LIGHTRED, [width/2, 0, width/2, height])
    #pygame.draw.rect(screen, BLACK, [width/2-outerradius, height/2-outerradius, 2*outerradius, 2*outerradius], 5)

    for i in range(2*sizeofgame):
        for j in range(2*sizeofgame):
            party = game.board[i][j]
            color = GREY
            if party == 0: #rep
                color = RED
            if party == 1:
                color = BLUE
            pygame.draw.rect(screen, color, [width/2-outerradius+i*blockwidth,height/2-outerradius+j*blockwidth , blockwidth, blockwidth])

    for i in clicked:
        pygame.draw.rect(screen, HIGHLIGHT, [width/2-outerradius+i[0]*blockwidth, height/2-outerradius+i[1]*blockwidth, blockwidth, blockwidth], 3)

    pygame.draw.rect(screen, GREY, [width/2+10, height/2+outerradius+10, outerradius-20, height/2 - outerradius - 20]) #gerrymender button
    gerrymanderbuttontext = font.render("GerryMander!", True, (0, 0, 0))
    screen.blit(gerrymanderbuttontext, (470, 567))

    pygame.draw.rect(screen, GREY, [width/2-10, height/2+outerradius+10, -outerradius+20, height/2 - outerradius - 20]) #giveup button

    demtext = bigfont.render(str(game.demPoint), True, BLUE)
    screen.blit(demtext, ((width/2-outerradius)/2-demtext.get_size()[0]/2, 50))

    reptext = bigfont.render(str(game.repPoint), True, RED)
    screen.blit(reptext, (width/2+outerradius+(width/2-outerradius)/2-demtext.get_size()[0]/2, 50))
    
    pygame.display.flip()

pygame.quit()
