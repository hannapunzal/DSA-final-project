# reference: https://gist.github.com/silversthem/4a9d220ccfaf8c0ec2290356f80eecc1
# the code has algorithm errors
# will try to change and add modifications like score, GUI, style, etc. if possible

import pygame
from pygame.locals import *
import random
# The 2048 grid
class Grid:
    def __init__(self): # Creates a new grid to play
        self.grid = [0 for k in range(16)]
    def randNew(self): # Generates a random new 2 or 4 tile in the grid
        freeTiles = [i for i in range(0,16) if self.grid[i] is 0] # Finding all free spaces
        self.hasMoved = False # Movement has ended, needs new movement
        if len(freeTiles) is 0:
            return False
        self.grid[freeTiles[random.randrange(len(freeTiles))]] = random.randint(1,2)*2
    def moveYAxis(self,d): # Moves along the Y axis, -1 for up and 1 for down
        for i in range(2 + 2*(-d),14 + 2*(-d)):
            if self.grid[i] is not 0 and (self.grid[i] is self.grid[i + 4*d] or self.grid[i + 4*d] is 0): # Testing if bottom/top tile matches this one or is empty
                self.hasMoved,self.grid[i],self.grid[i + 4*d] = True,0,self.grid[i + 4*d] + self.grid[i] # Changing current tile and top/bottom tile
                self.moveYAxis(d) # Recursive call to concatene until no more concatening
    def moveXAxis(self,d): # Moves along the X axis, -1 for left and 1 for right
        for i in range(4):
            for j in range((1 - d)/2,(1 - d)/2 + 3):
                if self.grid[i*4 + j] is not 0 and (self.grid[i*4 + j] is self.grid[i*4 + j + d] or self.grid[i*4 + j + d] is 0): # Testing if left/right tile matches this one or is empty
                    self.hasMoved,self.grid[i*4 + j],self.grid[i*4 + j + d] = True,0,self.grid[i*4 + j + d] + self.grid[i*4 + j] # Same principle has up/down
                    self.moveXAxis(d)
    def isDone(self): # If there's no move left
        return len([k for k in range(4) for j in range(3) if self.grid[k * 4 + j] is self.grid[k * 4 + j + 1] or self.grid[k * 4 + j] is 0] \
        + [k for k in range(3) for j in range(4) if self.grid[k * 4 + j] is self.grid[(k + 1)*4 + j] or self.grid[k*4 + j] is 0]) is 0 # Checking if there's no empty and identical tiles next to each other
    def render(self,win,background): # Prints the board on a 2048 window
        win.blit(background,(0,0))
        for i in range(4):
            for j in range(4):
                if self.grid[i * 4 + j] is not 0:
                    win.blit(pygame.font.Font(None, 50).render(str(self.grid[i * 4 + j]),2,(10,10,10)),(j * 100 + 20,i * 100 + 10))
# Grid
grid = Grid()
for i in range(3): grid.randNew()
# Game
pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption('2048')
# Board background
background = pygame.Surface((400,400)).convert()
background.fill((255,255,255))
# List of actions matching keys
action = {K_UP:lambda g : g.moveYAxis(-1),K_DOWN:lambda g : g.moveYAxis(1), # Up and Down
K_LEFT:lambda g : g.moveXAxis(-1),K_RIGHT:lambda g : g.moveXAxis(1)} # Left and right
# If the window is closed
closed = False
# Main loop
while not grid.isDone() and not closed:
    grid.render(win,background) # Printing the grid
    for event in pygame.event.get(): # Reading event
        closed = event.type is QUIT # If the window is closed
        if event.type is KEYDOWN: # Key pressed
            action.get(event.key,lambda x : x)(grid) # Get action matching key
    if grid.hasMoved: # The grid has moved
        grid.randNew() # Trying to put a new tile
    pygame.display.flip() # Refreshing the display
# End of game