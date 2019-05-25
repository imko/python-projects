import pygame
import game_functions as gf 

from pygame.sprite import Group 
from settings import Settings 
from ship import Ship 
from alien import Alien 
from game_stats import GameStats
from button import Button 
from scoreboard import ScoreBoard 

def run_game():
   # initialize pygame, settings, and screen object 
   pygame.init() 
   ai_settings = Settings() 
   screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # surface 
   pygame.display.set_caption('Alien Invasion')

   # make a ship, stats, a group of bullets and aliens 
   ship = Ship(ai_settings, screen)
   stats = GameStats(ai_settings)
   aliens = Group() 
   bullets = Group() 
   play_button = Button(ai_settings, screen, 'PLAY') 
   sb = ScoreBoard(ai_settings, screen, stats) 

   # create a fleet of aliens 
   gf.create_fleet(ai_settings, screen, ship, aliens) 

   # start the main loop for the game (manages screen update)
   while True: 
      # watch for keyboard and mouse events (event loop) 
      gf.check_events(ai_settings, screen, stats, play_button, sb, ship, bullets, aliens)

      if stats.game_active:
         ship.update() 
         gf.update_bullets(ai_settings, screen, sb, stats, ship, bullets, aliens) 
         gf.update_aliens(ai_settings, screen, stats, sb, ship, bullets, aliens)
      
      gf.update_screen(ai_settings, screen, stats, play_button, sb, ship, bullets, aliens)

run_game()