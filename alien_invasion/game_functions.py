import sys 
import pygame 

from bullet import Bullet 
from alien import Alien 

def check_events(ai_settings, screen, stats, play_button, sb, ship, bullets, aliens):
   '''Respond to keyboard / mouse events'''
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit() 
      elif event.type == pygame.KEYDOWN:
         check_keydown_event(event, ai_settings, screen, stats, ship, bullets)
      elif event.type == pygame.KEYUP: 
         check_keyup_event(ship, event)
      elif event.type == pygame.MOUSEBUTTONDOWN: 
         mouse_x, mouse_y = pygame.mouse.get_pos() 
         check_play_button(ai_settings, screen, stats, play_button, sb, mouse_x, mouse_y, ship, bullets, aliens)

def check_keydown_event(event, ai_settings, screen, stats, ship, bullets): 
   '''Check keydown event'''
   if event.key == pygame.K_q: 
      sys.exit() 
   if stats.game_active:
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

def check_play_button(ai_settings, screen, stats, play_button, sb, mouse_x, mouse_y, ship, bullets, aliens):
   '''Start a new game if play button is pressed'''
   if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active: 
      # reset the game except the high score 
      pygame.mouse.set_visible(False) 
      ai_settings.initialize_dynamic_settings() 
      stats.reset_stats() 
      stats.game_active = True 
      reset_game(ai_settings, screen, sb, ship, bullets, aliens)
      
def update_screen(ai_settings, screen, stats, play_button, sb, ship, bullets, aliens):
   '''Update images on the screen and flip to the new screen'''
   screen.fill(ai_settings.bg_color) # redraw screen during each pass 
   ship.blitme() # draw ship AFTER filling the background 
   aliens.draw(screen)
   
   # draw bullets 
   for bullet in bullets: 
      bullet.draw_bullet()

   # show everything one the scoreboard  
   sb.display_score()

   # draw 'PLAY' button if game is inactive 
   if not stats.game_active: 
      play_button.draw_button()

   pygame.display.flip() # make the most recently drawn screen visible (erases old screen so that only new screen is visible)

def update_bullets(ai_settings, screen, sb, stats, ship, bullets, aliens): 
   '''Update bullets and remove old bullets if necessary''' 
   bullets.update() # automatically calls bullet.update() in bullets

   # check for old bullets that are out of screen 
   for bullet in bullets.copy(): 
      if bullet.rect.bottom <= 0: 
         bullets.remove(bullet)

   # check for any bullets that have hit aliens, and remove if so 
   check_collision(ai_settings, screen, sb, stats, ship, bullets, aliens)

def update_aliens(ai_settings, screen, stats, sb, ship, bullets, aliens):
   '''Update positions of all aliens in the fleet'''
   check_fleet_edges(ai_settings, aliens)
   aliens.update() 

   # detect any collisions between ship and alien 
   if pygame.sprite.spritecollideany(ship, aliens):
      display_message('Aliens Got the Ship!')
      ship_hit(ai_settings, screen, stats, sb, ship, bullets, aliens)

   check_aliens_bottom(ai_settings, screen, stats, sb, ship, bullets, aliens) # check if aliens have reached the bottom 

def fire_bullet(ai_settings, screen, ship, bullets):
   '''Fire a bullet if limit is not reached'''
   if len(bullets) < ai_settings.bullet_allowed: 
      bullets.add(Bullet(ai_settings, screen, ship)) # add a bullet to the bullets 

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
   available_space_x = ai_settings.screen_width - (2 * alien.rect.width) # leaving spaces at each edge  
   available_space_y = ai_settings.screen_height - (4 * alien.rect.height - ship.rect.height) # 1 empty space on top, 3 empty spaces between alien and the ship
   
   return (int(available_space_y / (2 * alien.rect.height)), int(available_space_x / (2 * alien.rect.width)))  

def create_alien(ai_settings, screen, row_number, column_number, aliens): 
   '''Create and add an alien to the group of aliens'''
   alien = Alien(ai_settings, screen)
   
   # adjust position in x and y 
   alien.x = alien.rect.width + (2 * alien.rect.width * column_number) 
   alien.rect.x = alien.x 
   alien.y = alien.rect.height + (2 * alien.rect.height * row_number) + (alien.rect.height / 2)
   alien.rect.y = alien.y 

   aliens.add(alien) 

def check_fleet_edges(ai_settings, aliens): 
   '''Check if any one of the aliens has reachced an edge and respond appropriately'''
   for alien in aliens.sprites(): 
      if alien.at_edge():
         change_fleet_direction(ai_settings, aliens)
         break

def change_fleet_direction(ai_settings, aliens):
   '''Drop the fleet by fleet drop speed and change direction''' 
   for alien in aliens.sprites():
      alien.rect.y += ai_settings.fleet_drop_speed 

   ai_settings.fleet_direction *= -1 # change direction 

def check_collision(ai_settings, screen, sb, stats, ship, bullets, aliens):
   '''Check collision and respond appropriately'''
   # collision := dictionary with (bullet, list of aliens)
   collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) 
   if collisions: # update score if hit 
      # number of aliens (value) hit by bullet (key) 
      for aliens in collisions.values(): 
         stats.score += (ai_settings.alien_points * len(aliens)) 
         sb.prep_score() # update score if for any hit aliens 
      check_high_score(sb, stats) # check if current score is higher than the high score 

   # create a new fleet if the user shoots all existing aliens and advance to the next wave 
   if len(aliens) == 0: 
      advance_to_next_wave(ai_settings, screen, sb, stats, ship, bullets, aliens)  

def advance_to_next_wave(ai_settings, screen, sb, stats, ship, bullets, aliens):
   '''Update statistics and settings, and advance to the next wave'''
   bullets.empty() 
   ai_settings.increase_speed() 
   stats.level += 1
   sb.prep_level() 
   create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, screen, stats, sb, ship, bullets, aliens): 
   '''Respond to ship being hit by alien'''
   # check if the player still has ships available 
   if stats.available_ships > 0:
      stats.available_ships -= 1 
      reset_game(ai_settings, screen, sb, ship, bullets, aliens)
   else: # game over 
      stats.game_active = False 
      pygame.mouse.set_visible(True) 

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, bullets, aliens):
   '''Detects any alien that got to the bottom of the screen''' 
   for alien in aliens.sprites(): 
      # check if the alien reached the bottom 
      if alien.rect.bottom >= screen.get_rect().bottom: 
         # same logic as when aliens collide with the ship 
         display_message('Aliens Reached the Bottom!') 
         ship_hit(ai_settings, screen, stats, sb, ship, bullets, aliens)
         break 

def display_message(message): 
   '''Display message how the current wave ended'''
   print(message)
   pygame.time.wait(1500) # wait for 1.5 seconds

def reset_game(ai_settings, screen, sb, ship, bullets, aliens):
   '''Reset game to start'''
   # reset lists of bullets and aliens 
   bullets.empty()
   aliens.empty() 

   reset_scoreboard(sb)

   # create a new fleet and center the ship 
   create_fleet(ai_settings, screen, ship, aliens)
   ship.center_ship() 

def reset_scoreboard(sb):
   '''Reset / update scoreboard''' 
   sb.prep_score() 
   sb.prep_high_score() 
   sb.prep_level() 
   sb.prep_ship() 

def check_high_score(sb, stats): 
   '''Check and update high score if necessary'''
   if stats.score > stats.high_score: 
      stats.high_score = stats.score 
      sb.prep_high_score() 
