import pygal 

from die import Die

die1 = Die() 
die2 = Die() 
die3 = Die() 

results = list() 
for roll_number in range(1000):
   results.append(die1.roll() + die2.roll() + die3.roll()) 

freq = list() 
for value in range(3, die1.number_sides + die2.number_sides + die3.number_sides + 1): 
   freq.append(results.count(value)) 

hist = pygal.Bar() 

# set title and label axes for the histogram 
hist.title = 'Results of rolling ' + str(len(results)) + ' times'
hist.x_labels = [x for x in range(3 ,die1.number_sides + die2.number_sides + die3.number_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', freq)
hist.render_to_file('die_visual.svg')