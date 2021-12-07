import requests


import json
from datetime import datetime

URL = "https://www.reddit.com/r/entertainment/.json"


def timestamp_to_date(timestamp_object):
    datetime_object = datetime.fromtimestamp(timestamp_object)
    return str(datetime_object)

def get_data(url):
    response = requests.get(url,headers={'User-agent':"your bot 0.1"})
    json_object = response.text
    python_object = json.loads(json_object)
    news = python_object['data']['children']
    data = []
    number = 1
    for new in news:
        news_dictionary = {
            f'News No. {number}':{
                'title': new['data']['title'],
                'created': timestamp_to_date(new['data']['created']),
                'author':new['data']['author']
            }
        }
        number +=1
        data.append(news_dictionary)
    return data


def write_to_json(some_data):
    with open('RedditNews.json','w') as file:
        json.dump(some_data,file,indent=4)


def main(url):
    data = get_data(url)
    write_to_json(data)


main(URL)
