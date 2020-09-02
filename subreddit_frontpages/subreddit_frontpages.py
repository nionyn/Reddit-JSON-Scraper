import requests
import json
import time
import os

subs_to_watch = ['news', 'worldnews', 'politics']
agent = 'fpbotv_n0.1'

def get_time():
    return str(int(time.time()))

def get_sub_snapshot(sub):
    url = 'https://www.reddit.com/r/' + sub + '/.json'
    r = requests.get(url, headers = {'User-agent': agent}).json()
    filename = 'downloaded/frontpages/' + sub + '/' + get_time() + '.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(r, f)

## main
for sub in subs_to_watch:
    #get sub snapshot
    get_sub_snapshot(sub)
    print('retrieved front page of '+sub)
    print('delaying for 5 seconds')
    time.sleep(5)
    
    
