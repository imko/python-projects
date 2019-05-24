class Settings():

   '''A class to store all settings for Alien Invasion'''

   def __init__(self):
      '''Initialize the game's settings'''
      # screen settings 
      self.screen_width = 1200
      self.screen_height = 700
      self.bg_color = (230, 230, 230) # white

      # ship settings 
      self.ship_speed_factor = 4.5 

      # bullet settings 
      self.bullet_speed_factor = 2.5 
      self.bullet_width = 3 
      self.bullet_height = 15 
      self.bullet_color = (60, 60, 60) 
      self.bullet_allowed = 3 