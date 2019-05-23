import pygame 

from pygame.sprite import Sprite 

class Bullet(Sprite): 
   '''A class to manage bullets fired from the ship'''

   def __init__(self, ai_settings, screen, ship):
      '''Create a bullet object at the ship's current position'''
      super(Bullet, self).__init__() 
      self.screen = screen 
      
      # create a bullet rect a (0, 0), then set correct position 
      self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # initialize Rect class (left, right, width, height)
      self.rect.centerx = ship.rect.centerx 
      self.rect.top = ship.rect.top 

      # store the bullet's position as a decimal value, for fine adjustments 
      self.y = float(self.rect.y) 

      self.color = ai_settings.bullet_color 
      self.speed_factor = ai_settings.bullet_speed_factor 

   def update(self): 
      '''Move the bullet up the screen'''
      self.y -= self.speed_factor # update position of the bullet 
      self.rect.y = self.y # update rect position 

   def draw_bullet(self): 
      '''Draw the bullet on the screen''' 
      pygame.draw.rect(self.screen, self.color, self.rect) 