import sys 
import pygame 

from bullet import Bullet 

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

def check_keyup_event(ship, event):
   '''Check keyup event'''
   if event.key == pygame.K_RIGHT:
      ship.moving_right = False 
   elif event.key == pygame.K_LEFT:
      ship.moving_left = False 
      
def update_screen(ai_settings, screen, ship, bullets):
   '''Update images on the screen and flip to the new screen'''
   screen.fill(ai_settings.bg_color) # redraw screen during each pass 
   ship.blitme() # draw ship AFTER filling the background 
   
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