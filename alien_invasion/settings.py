class Settings():

   '''A class to store all settings for Alien Invasion'''

   def __init__(self):
      '''Initialize the game's settings'''
      # screen settings 
      self.screen_width = 1200
      self.screen_height = 700
      self.bg_color = (230, 230, 230) # white

      # ship settings
      self.ship_limit = 3 

      # bullet settings 
      self.bullet_width = 800 
      self.bullet_height = 15 
      self.bullet_color = (60, 60, 60) 
      self.bullet_allowed = 3 

      # alien settings  
      self.fleet_drop_speed = 20 

      self.speed_up_scale = 1.1 
      self.score_scale = 1.5 

      self.initialize_dynamic_settings()

   def initialize_dynamic_settings(self):
      self.ship_speed_factor = 4.5 
      self.bullet_speed_factor = 2.5 
      self.alien_speed_factor = 5 
      self.fleet_direction = 1 # 1 = right, -1 = left 
      self.alien_points = 50 

   def increase_speed(self):
      self.ship_speed_factor *= self.speed_up_scale
      self.bullet_speed_factor *= self.speed_up_scale
      self.alien_speed_factor *= self.speed_up_scale 
      self.alien_points = int(self.alien_points * self.score_scale)