import pygame

import game_functions as gf 

from settings import Settings 
from ship import Ship 
from character import Character 

def run_game():
   # Initialize pygame, settings, and screen object 
   pygame.init() 
   ai_settings = Settings() 
   screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # surface 
   pygame.display.set_caption('Alien Invasion')

   # Make a ship 
   ship = Ship(screen)
   character = Character(screen) 

   # Start the main loop for the game (manages screen update)
   while True: 
      # Watch for keyboard and mouse events (event loop)
      gf.check_events() 
      gf.update_screen(ai_settings, screen, ship, character)  

run_game()