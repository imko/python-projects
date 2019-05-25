'''
   A random walk is a path that has no clear direction,
   but is determined by a series of random decisions. 
   --> Taking every step in a random direction
'''

from random import choice 

class RandomWalk(): 
   '''A class to generate random walks'''

   def __init__(self, num_points=5000): 
      '''Initialize attributes of a walk'''
      self.num_points = num_points 

      # all walks start at (0, 0)
      self.x_values = [0]
      self.y_values = [0]

   def fill_walk(self): 
      '''Calculate all the points in the walk'''
      while len(self.x_values) < self.num_points:
         # decide which direction and distance to go from current position 
         x_step = self.get_step() 
         y_step = self.get_step() 

         # reject any moves that go nowhere 
         if x_step == 0 and y_step == 0: 
            continue

         # calculate next steps by adding the current position and the next step, and append to the lists 
         x_next = self.x_values[-1] + x_step 
         y_next = self.y_values[-1] + y_step

         self.x_values.append(x_next)
         self.y_values.append(y_next)

   def get_step(self): 
      direction = choice([-1, 1]) 
      distance = choice(range(5)) # from 0 - 4 steps 
      
      return direction * distance 