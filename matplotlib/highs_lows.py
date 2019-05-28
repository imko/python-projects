import csv 

from matplotlib import pyplot as plt 
from datetime import datetime

def plot_data(filename): 
   with open(filename) as f: 
      reader = csv.reader(f)
      header_row = next(reader) # skips header row 

      # to see format of the data 
      # for index, column_header in enumerate(header_row): 
      #    print(index, column_header)
      
      # dates := a list of datetime objects 
      # handles any data that are missing 
      dates, lows, highs = list(), list(), list()
      for row in reader: 
         try: 
            current_date = datetime.strptime(row[0], '%Y-%m-%d') 
            low = int(row[2])
            high = int(row[1])
         except ValueError: 
            print(current_date, 'missing data')
         else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

   return (dates, lows, highs)

# get date, low temps, and high temps from the file 
l1 = plot_data('./data/death_valley_2014.csv')
l2 = plot_data('./data/sitka_weather_2014.csv')
# filename = './data/sitka_weather_07-2014.csv'
# filename = './data/death_valley_2014.csv' # data of 2014 

# plot data and save PNG
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(l1[0], l1[1], c='red', alpha=0.5)
plt.plot(l1[0], l1[2], c='blue', alpha=0.5)
plt.plot(l2[0], l2[1], c='green', alpha=0.5)
plt.plot(l2[0], l2[2], c='yellow', alpha=0.5)
plt.fill_between(l1[0], l1[1], l1[2], facecolor='blue', alpha=0.1) # shading the area between the two y-values 
plt.fill_between(l2[0], l2[1], l2[2], facecolor='green', alpha=0.1) 
# plt.savefig('highs_low.png', bbox_inches='tight')

# set plot title and label its axes
# plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.title('Daily low and high temperatures', fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
fig.autofmt_xdate() # prevents overlapping

plt.show()