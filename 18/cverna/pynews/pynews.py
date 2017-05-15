import requests

max_item = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json')

for item in range (10000000, max_item.json()):
    story = requests.get(
        'https://hacker-news.firebaseio.com/v0/item/{}.json'.format(item)).json()
    if story is not None and 'story' == story.get('type', ''):
        if 'python' in story.get('title', '').lower():
           data = {'title': story['title'], 'url': story['url'], 'score': story['score']}
           requests.post('http://127.0.0.1:5000/add', json=data)
