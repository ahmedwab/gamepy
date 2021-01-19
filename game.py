# Importing the pygame module
import pygame

# game local commads
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

# Display width and height
displaySIZE = (800,600)
centerDisplay = (400,300)

# Game Background Color

backgroundColor = (50,245,245)

gameRunning = True
while gameRunning:
    display = pygame.display.set_mode(displaySIZE)
    

    for event in pygame.event.get():
        
        # User input key
        if event.type == KEYDOWN:
            # User presses escape
            if event.key == K_ESCAPE:
                gameRunning = False


        # If user quits
        elif event.type == QUIT:
            gameRunning = False
    
    pygame.display.set_caption('Python game')
    display.fill(backgroundColor)
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    display.blit(surf, centerDisplay)
    pygame.display.flip()

  