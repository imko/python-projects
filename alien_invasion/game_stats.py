class GameStats():
   '''Track statistics for Alien Invasion'''

   def __init__(self, ai_settings):
      '''Initialize game stats'''
      self.ai_settings = ai_settings 
      self.reset_stats()
      self.game_active = False
      
      # load high score if it exists 
      filename = 'high_score.txt'
      try: 
         with open(filename, 'r') as file_object:
            self.high_score = file_object.read().strip() 
         self.high_score = int(self.high_score)
      except: 
         self.high_score = 0 

   def reset_stats(self):
      '''Reset statistics to initial settings'''
      self.available_ships = self.ai_settings.ship_limit
      self.score = 0 
      self.level = 1 
