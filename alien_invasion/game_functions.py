import sys 
import pygame 

def check_events():
   ''' Respond to keyboard / mouse events '''
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit() 

def update_screen(ai_settings, screen, *elements):
   ''' Update images on the screen and flip to the new screen '''
   screen.fill(ai_settings.bg_color) # redraw screen during each pass 
   for element in elements:
      element.blitme() # draw ship AFTER filling the background 

   pygame.display.flip() # make the most recently drawn screen visible (erases old screen so that only new screen is visible)