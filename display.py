import pygame
import main

sizeofgame = 4
game = main.Game(sizeofgame)
pygame.init()

#Define the colors we will use in RGB format
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
GREY = (100, 100, 100)
# Set the height and width of the screen
size  = [800,600]
width = size[0]
height = size[1]

#game size etc
outerradius = 250
innerradius = 230
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

    
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [width/2-outerradius, height/2-outerradius, 2*outerradius, 2*outerradius], 5)

    for i in range(2*sizeofgame):
        for j in range(2*sizeofgame):
            party = game.board[i][j]
            color = GREY
            if party == 0: #rep
                color = RED
            if party == 1:
                color = BLUE
            pygame.draw.rect(screen, color, [width/2-outerradius+i*blockwidth,height/2-outerradius+j*blockwidth , blockwidth, blockwidth])
    
    pygame.display.flip()

pygame.quit()
