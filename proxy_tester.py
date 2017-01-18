# better version
# Import github.com/yousefissa
# @devmykal helped me bc im a nut

import time
from requests import Session
import multiprocessing

session = Session()
session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'})

def mil_seconds():
    return int(round(time.time() * 1000))

def proxyChecker(proxy):
    session.proxies.update({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    for url in sites:
        start_time = mil_seconds()
        try:
	        response = session.get(url)
	        print(response.status_code)
	        if response.status_code != 200:
	            print(proxy, ' is not a good proxy.')
	        else:
	            print('[{}] on site {} ---- {} ms'.format(proxy, url, mil_seconds() - start_time))
        except: # broad exceptions are bad but who cares
        	print('Bad Proxy {} on {}'.format(proxy, url))

# MAIN
# gets proxies in a text file, rather than hard-coding them
with open("proxies.txt") as proxies_text:
    proxies = proxies_text.read().splitlines()

print('Currently loaded:', proxies)

if proxies == []:
    print('You did not load proxies. Check your proxies.txt file!')
    exit()

# input the sites you want to test against here.
sites = [
    'http://google.com/',
    'http://www.footlocker.com/',
    'http://www.eastbay.com/',
    'http://www.supremenewyork.com/shop']
print('Testing on sites ', sites)


jobs = []
for p in proxies:
    m = multiprocessing.Process(target=proxyChecker, args=(p,))
    jobs.append(m)

for j in jobs:
    j.start()