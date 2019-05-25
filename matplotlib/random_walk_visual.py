import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
   # make a random walk, and plot points 
   rw = RandomWalk(50000) 
   rw.fill_walk() 

   # plt.title('Random Walk', fontsize=24) # set plot title
   plt.figure(figsize=(10, 6)) # set the size of plot window 
   plt.axes().set_axis_off() # remove axes

   # color points 
   point_numbers = list(range(rw.num_points)) 
   plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

   # emphasize on first and last points 
   plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor='none' , s=25)
   plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=25)

   plt.show()

   user_input = input('Make another walk? (y/n): ')
   if user_input == 'n': 
      break