from Board import *
from Variables import *

import pygame
pygame.init()
clock = pygame.time.Clock()
BackGroundImage = pygame.image.load(Background)
PageImage = pygame.image.load(Page)
sound = pygame.mixer.Sound("sound1.mp3")
window = pygame.display.set_mode(WindowSize)
COLOR = (255, 0, 0)
class Interface:

    while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit

     #window.fill((255, 255, 255))


     if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()
            pygame.draw.circle(PageImage, COLOR, pos, 4)


     window.blit(BackGroundImage, (0, 0))
     window.blit(PageImage, PageOnScreen)
     pygame.mixer.Sound.play(sound)
     pygame.display.flip()
     if COLOR == (255, 0, 0):
         COLOR = (0, 0, 0)
     else:
         COLOR = (255, 0, 0)





   # def __init__(self, x, y, image):

#    def update(self):
      # pass
#
 #   def setDot(self, surface):
          #  surface.blit(self.image, (self.x, self.y))
#
#    def SetDot_GetDot(self):  # applying interface substitution principle
       # pos = pygame.mouse.get_pos()
       # pygame.draw.circle(PageImage, Color, pos, DotRadius)
      #  pygame.display.update()

    # Create a new object with an image
#obj = Interface(100, 100, pygame.image.load(PageImage))




