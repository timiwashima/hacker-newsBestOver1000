# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 08:18:27 2023
Print the "Best" news stories from hacker-news.com with scores over 1000
@author: tiwashima
"""

import requests
import datetime

url='https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty'
r=requests.get(url)

#Check if the Database is accessible
#access=r.status_code
#if access==200:
#    print("Database accessible")
#else:
#    print("Database not accessible")

responseDict=r.json()
#See raw response list
#print(responseDict.keys())

for articleNumber in range(0,len(responseDict)):
    #add each article number to the base URL
    #print('https://hacker-news.firebaseio.com/v0/item/' + str(responseDict[articleNumber]) + '.json')
    articleResponse='https://hacker-news.firebaseio.com/v0/item/' + str(responseDict[articleNumber]) + '.json'
    a=requests.get(articleResponse)
    articleDict=a.json()
    if articleDict['score'] > 1000:
        time=articleDict['time']
        articleTime=datetime.datetime.fromtimestamp(time).strftime('%c')
        print(articleDict['title'])
        print('By: ' + articleDict['by'])
        print(articleTime)
        print(articleDict['url'])
        print()