import pygame.font 

from pygame.sprite import Group

from ship import Ship 

class ScoreBoard(): 
   '''A class to store scoring information'''

   def __init__(self, ai_settings, screen, stats): 
      '''Initialize score board''' 
      self.ai_settings = ai_settings
      self.screen = screen 
      self.screen_rect = screen.get_rect() 
      self.stats = stats 

      self.text_color = (30, 30, 30)
      self.font = pygame.font.Font(None, 48)

      # prep all elements on scoreboard 
      self.prep_score() 
      self.prep_high_score() 
      self.prep_level() 
      self.prep_ship()

   def prep_score(self): 
      '''Render score image and set its position at top-right'''
      score = "{:,}".format(int(round(self.stats.score, -1))) # rounds to nearest multiple of 10 
      self.score_image = self.font.render(score, True, self.text_color, self.ai_settings.bg_color) 

      # score board position on top-right 
      self.score_rect = self.score_image.get_rect() 
      self.score_rect.right = self.screen_rect.right - 20 
      self.score_rect.top = 20 

   def prep_high_score(self): 
      '''Update high score and set its position at top-center'''
      high_score = "{:,}".format(int(round(self.stats.high_score, -1))) 
      self.high_score_image = self.font.render(high_score, True, self.text_color, self.ai_settings.bg_color)

      # high score board position at top-center 
      self.high_score_rect = self.high_score_image.get_rect() 
      self.high_score_rect.center = self.screen_rect.center 
      self.high_score_rect.top = self.score_rect.top 

   def prep_level(self):
      '''Update level and set its position at top-right, below score board'''
      level = str(self.stats.level) 
      self.level_image = self.font.render(level, True, self.text_color, self.ai_settings.bg_color)

      # level board position on top-right below score board 
      self.level_rect = self.level_image.get_rect() 
      self.level_rect.right = self.screen_rect.right - 20 
      self.level_rect.top = self.score_rect.bottom  

   def prep_ship(self):
      '''Update the number of available ships and set its position at top-left'''
      self.ships = Group() 
      for number_ships in range(self.stats.available_ships): 
         ship = Ship(self.ai_settings, self.screen) 
         ship.rect.x = 10 + number_ships * ship.rect.width # 10 px in between 
         ship.rect.y = self.score_rect.top # adjust to scoreboard height 
         self.ships.add(ship) 

   def display_score(self):
      '''Draw score board on the screen'''
      self.screen.blit(self.score_image, self.score_rect)
      self.screen.blit(self.high_score_image, self.high_score_rect)
      self.screen.blit(self.level_image, self.level_rect) 
      self.ships.draw(self.screen) 