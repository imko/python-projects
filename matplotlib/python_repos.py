import requests 
import pygal 

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code:', r.status_code)
r_dict = r.json() 
print('Total repositories: ', r_dict['total_count'])
print('Repositories returned: ', len(r_dict['items']))

repo_dicts = r_dict['items']

names, plot_dicts = list(), list() 
for repo_dict in repo_dicts: 
   names.append(repo_dict['name'])
   description = repo_dict['description']
   if not description: 
      description = 'No description'

   plot_dict = {
      'value': repo_dict['stargazers_count'],
      'label': description,
      'xlink': repo_dict['html_url'],
   }

   plot_dicts.append(plot_dict)

# make visualization 
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config() 
my_config.x_label_rotation = 45
my_config.show_legend = False 
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18 
my_config.truncate_label = 15 # shorten label to 15 characters 
my_config.show_y_guides = False 
my_config.width = 1000 

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names 

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# for repo_dict in repo_dicts: 
#    print('Name:', '\t', repo_dict['name'])
#    print('Owner:', '\t', repo_dict['owner']['login'])
#    print('Stars:', '\t', repo_dict['stargazers_count'])
#    print('Repository:', '\t', repo_dict['html_url'])
#    print('Description:', '\t', repo_dict['description'], '\n')
