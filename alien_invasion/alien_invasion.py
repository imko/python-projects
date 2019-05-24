import pygame
import game_functions as gf 

from pygame.sprite import Group 
from settings import Settings 
from ship import Ship 
from alien import Alien 

def run_game():
   # initialize pygame, settings, and screen object 
   pygame.init() 
   ai_settings = Settings() 
   screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # surface 
   pygame.display.set_caption('Alien Invasion')

   # make a ship, a group of bullets and aliens 
   ship = Ship(ai_settings, screen)
   # alien = Alien(ai_settings, screen)
   aliens = Group() 
   bullets = Group() 

   # create a fleet of aliens 
   gf.create_fleet(ai_settings, screen, ship, aliens) 

   # start the main loop for the game (manages screen update)
   while True: 
      # watch for keyboard and mouse events (event loop) 
      gf.check_events(ai_settings, screen, ship, bullets) 
      ship.update() 
      gf.update_bullets(bullets) 
      gf.update_aliens(ai_settings, aliens)
      gf.update_screen(ai_settings, screen, ship, bullets, aliens) 

run_game()