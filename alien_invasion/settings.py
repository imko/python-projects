class Settings():

   '''A class to store all settings for Alien Invasion'''

   def __init__(self):
      '''Initialize the game's settings'''
      # screen settings 
      self.screen_width = 1250
      self.screen_height = 750
      self.bg_color = (230, 230, 230) # white

      # ship settings
      self.ship_limit = 2 

      # bullet settings 
      self.bullet_width = 5 
      self.bullet_height = 25 
      self.bullet_color = (60, 60, 60) 
      self.bullet_allowed = 5 

      # alien settings  
      self.fleet_drop_speed = 15 

      # score settings 
      self.speed_up_scale = 1.2 
      self.score_scale = 1.5 

      self.initialize_dynamic_settings()

   def initialize_dynamic_settings(self):
      '''Initialize any settings that are dynamic (ie. attributes that change during the game)'''
      self.ship_speed_factor = 4.5 
      self.bullet_speed_factor = 2.5 
      self.alien_speed_factor = 5 
      self.fleet_direction = 1 # 1 = right, -1 = left 
      self.alien_points = 50 

   def increase_speed(self):
      '''Increase speed/points by a fixed scale''' 
      self.ship_speed_factor *= self.speed_up_scale
      self.bullet_speed_factor *= self.speed_up_scale
      self.alien_speed_factor *= self.speed_up_scale 
      self.alien_points = int(self.alien_points * self.score_scale)