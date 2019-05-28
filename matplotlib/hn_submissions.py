import requests

from operator import itemgetter 

# make an API call and store the response 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code:', r.status_code)

# process info about each submission 
submissions_ids = r.json() 
submissions_dicts = list()

for submission_id in submissions_ids[:30]: 
   url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
   r = requests.get(url)
   
   print('Status code:', r.status_code)
   response_dict = r.json() 
   submission_dict = {
      'title': response_dict['title'],
      'link': 'https://news.ycombinator.com/item?id=' + str(submission_id),
      'comments': response_dict.get('descendants', 0) # dict.get() returns 0 if not in dict 
   }

   submissions_dicts.append(submission_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True) 

for submission_dict in submissions_dicts: 
   print('\nTitle:', submission_dict['title'])
   print('Link:', submission_dict['link'])
   print('Comments:', submission_dict['comments'])