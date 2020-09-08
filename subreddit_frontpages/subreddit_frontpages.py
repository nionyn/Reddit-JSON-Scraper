import requests
import json
import time
import os
import config

#which subreddits to retrieve
subs_to_watch = config.subs_to_watch
#give agent a unique name
agent = config.agent

#function to return time in unix format
def get_time():
    return str(int(time.time()))

#function to get reddit page and store it as a json file
def get_sub_snapshot(sub):
    #build url string of subreddit
    url = 'https://www.reddit.com/r/' + sub + '/.json'
    #make a request to reddit using the url
    r = requests.get(url, headers = {'User-agent': agent}).json()
    #filename = folder + subreddit + unix time stamp + .json
    filename = 'downloaded/frontpages/' + sub + '/' + get_time() + '.json'
    #ensure directories already exist, if not create them
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    #open a filehandler and store the json
    with open(filename, 'w') as f:
        json.dump(r, f)

## main
for sub in subs_to_watch:
    #get sub snapshot
    get_sub_snapshot(sub)
    print('retrieved front page of '+sub)
    #introduce a delay to ensure server does not rate limit
    print('delaying for 5 seconds')
    time.sleep(5)
    
    
