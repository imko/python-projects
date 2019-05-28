import json
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES # dictionary with two-digit country codes 

def get_country_code(country_name):
   for code, name in COUNTRIES.items():
      if name == country_name: 
         return code 
   
   return None 

def view_world_map():
   wm = World() 
   wm.title = 'North, Central, and South America'

   wm.add('North America', ['ca', 'mx', 'us'])
   wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
   wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

   wm.render_to_file('americas.svg')

filename = './data/population_data.json'
with open(filename) as f: 
   pop_list = json.load(f)

cc_pop1, cc_pop2, cc_pop3 = dict(), dict(), dict() 
for pop_dict in pop_list: 
   if pop_dict['Year'] == '2010':
      country_code = get_country_code(pop_dict['Country Name'])
      pop = int(float(pop_dict['Value']))
      if pop < 10000000:
         cc_pop1[country_code] = pop
      elif pop < 1000000000:
         cc_pop2[country_code] = pop 
      else:
         cc_pop3[country_code] = pop

wm = World() 
wm.title = 'World Population in 2010, by country'
wm.add('< 10M', cc_pop1)
wm.add('10M-1B', cc_pop2)
wm.add('> 1B', cc_pop3)

wm.render_to_file('world_population.svg')