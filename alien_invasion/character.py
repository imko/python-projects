import pygame 

class Character():
   ''' A class that stores data of Character '''

   def __init__(self, screen):
      self.screen = screen 

      # load the character image and get its rect 
      self.image = pygame.image.load('images/character.png')
      self.rect = self.image.get_rect() 
      self.screen_rect = screen.get_rect() 

      # start each character at the center of the screen 
      self.rect.centerx = self.screen_rect.centerx
      self.rect.centery = self.screen_rect.centery

   def blitme(self):
      ''' Draw the character at its current position '''
      self.screen.blit(self.image, self.rect)