# lets import our modules
import pygame
from pygame.locals import *
from pathlib import Path
from Variables import *
import sys
from Interface import *
BASE_PATH = Path(__file__).resolve().parent

class Board:

 # lets start creating our board world
 pygame.init()
window = pygame.display.set_mode(WindowSize)
clock = pygame.time.Clock()
BackGroundImage = pygame.image.load(Background)
PageImage = pygame.image.load(Page)
sound = pygame.mixer.Sound("sound1.mp3")
#pygame.draw.rect(PageImage, (0,0,0), (140, 20, 10, 10))
while True:
    COLOR = (255, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        window.fill((255, 255, 255))


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(PageImage, (0, 0, 0), pos, 4)
            print(pos)

    window.blit(BackGroundImage, (0, 0))
    window.blit(PageImage, PageOnScreen)
    pygame.mixer.Sound.play(sound)

    pygame.display.flip()
    clock.tick(Refresh)
