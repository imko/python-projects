import pygame 

from pygame.sprite import Sprite 

class Alien(Sprite):
   '''A class that holds data for a single alien in the fleet'''
   
   def __init__(self, ai_settings, screen):
      super(Alien, self).__init__() 
      self.screen = screen # mostly used for blit 
      self.ai_settings = ai_settings 

      # load the alien image and get its rect attributes 
      self.image = pygame.image.load('images/alien.bmp')
      self.rect = self.image.get_rect() 
      self.screen_rect = screen.get_rect() 

      # start new alien near top-left of the screen 
      self.rect.x = self.rect.width 
      self.rect.y = self.rect.height 

      # store exact position of the alien 
      self.x = float(self.rect.x) 
      self.y = float(self.rect.y)

   def blitme(self): 
      self.screen.blit(self.image, self.rect)