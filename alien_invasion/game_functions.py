import sys 
import pygame 

from bullet import Bullet 
from alien import Alien 

def check_events(ai_settings, screen, ship, bullets):
   '''Respond to keyboard / mouse events'''
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit() 
      elif event.type == pygame.KEYDOWN:
         check_keydown_event(event, ai_settings, screen, ship, bullets)
      elif event.type == pygame.KEYUP: 
         check_keyup_event(ship, event)

def check_keydown_event(event, ai_settings, screen, ship, bullets): 
   '''Check keydown event'''
   if event.key == pygame.K_RIGHT:
      ship.moving_right = True 
   elif event.key == pygame.K_LEFT:
      ship.moving_left = True 
   elif event.key == pygame.K_SPACE: 
      fire_bullet(ai_settings, screen, ship, bullets)
   elif event.key == pygame.K_q: 
      sys.exit() 

def check_keyup_event(ship, event):
   '''Check keyup event'''
   if event.key == pygame.K_RIGHT:
      ship.moving_right = False 
   elif event.key == pygame.K_LEFT:
      ship.moving_left = False 
      
def update_screen(ai_settings, screen, ship, bullets, aliens):
   '''Update images on the screen and flip to the new screen'''
   screen.fill(ai_settings.bg_color) # redraw screen during each pass 
   ship.blitme() # draw ship AFTER filling the background 
   # aliens.blitme() # draw alien AFTER filling the background 
   aliens.draw(screen)
   
   # draw bullets 
   for bullet in bullets: 
      bullet.draw_bullet()

   pygame.display.flip() # make the most recently drawn screen visible (erases old screen so that only new screen is visible)

def update_bullets(bullets): 
   '''Update bullets and remove old bullets if necessary''' 
   bullets.update() # automatically calls update() in bullets Group 

   # check for old bullets that are out of screen 
   for bullet in bullets.copy(): 
      if bullet.rect.bottom <= 0: 
         bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
   '''Fire a bullet if limit is not reached'''
   if len(bullets) < ai_settings.bullet_allowed: 
      bullets.add(Bullet(ai_settings, screen, ship))

def create_fleet(ai_settings, screen, ship, aliens):
   '''Create a full fleet of aliens'''
   # create an alien to find the possible number of aliens in a row 
   # spacing between each alien is equal to one alien width 
   number_rows, number_columns = get_number_aliens_x_y(ai_settings, screen, ship)

   # create and place in available rows and columns 
   for row_number in range(number_rows): 
      for column_number in range(number_columns):
         create_alien(ai_settings, screen, row_number, column_number, aliens) 

def get_number_aliens_x_y(ai_settings, screen, ship): 
   '''Calculate and return number of available spaces in tuple'''
   alien = Alien(ai_settings, screen)
   available_space_x = ai_settings.screen_width - (2 * alien.rect.width) # leaving spaces at edges 
   available_space_y = ai_settings.screen_height - (3 * alien.rect.height - ship.rect.height) # 1 empty space on top, 2 empty spaces between alien and the ship
   
   return (int(available_space_y / (2 * alien.rect.height)), int(available_space_x / (2 * alien.rect.width)))  

def create_alien(ai_settings, screen, row_number, column_number, aliens): 
   alien = Alien(ai_settings, screen)
   
   # adjust position in x and y 
   alien.x = alien.rect.width + (2 * alien.rect.width * column_number) 
   alien.rect.x = alien.x 
   alien.y = alien.rect.height + (2 * alien.rect.height * row_number)
   alien.rect.y = alien.y 

   aliens.add(alien) 