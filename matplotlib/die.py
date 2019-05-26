from random import randint 

class Die():
   '''A class representing a single die''' 

   def __init__(self, number_sides=6):
      '''Initialize to standard die'''
      self.number_sides = number_sides 

   def roll(self):
      return randint(1, self.number_sides)