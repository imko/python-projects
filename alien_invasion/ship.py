import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
   '''A class that stores data of Ship'''

   def __init__(self, ai_settings, screen):
      '''Initialize the ship and set its starting position'''
      super(Ship, self).__init__() 
      self.screen = screen
      self.ai_settings = ai_settings 

      # load the ship image and get its rect attributes  
      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect() 
      self.screen_rect = screen.get_rect() 

      # you can set any of x-/y-coordinates of top, bottom, left, ride edges of rect 
      # start each new ship at the bottom center of the screen 
      self.rect.centerx = self.screen_rect.centerx 
      self.rect.bottom = self.screen_rect.bottom 

      # flag for continuous movement 
      self.moving_right = False 
      self.moving_left = False 

      self.center = float(self.rect.centerx) # because rect.centerx only takes int 

   def update(self):
      '''Update the position based on the movement flag'''
      if self.moving_right and self.rect.right < self.screen_rect.right: 
         self.center += self.ai_settings.ship_speed_factor
      if self.moving_left and self.rect.left > 0:
         self.center -= self.ai_settings.ship_speed_factor

      self.rect.centerx = self.center # decimal points will be truncated since self.rect.centerx is int 

   def blitme(self):
      '''Draw the ship at its current position'''
      self.screen.blit(self.image, self.rect)

   def center_ship(self):
      '''Center the ship on the screen'''
      self.center = float(self.screen_rect.centerx)