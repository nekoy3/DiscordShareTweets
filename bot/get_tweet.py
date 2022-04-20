import global_value as g

import twint
import csv
import os

async def get_tweet_csv(twitter_username, search_word):
    c = twint.Config()
    if twitter_username != '':
        c.Username = twitter_username
    c.Search = search_word
    c.Limit = g.LIMIT_SCRAPING_DAY_COUNT
    c.Output = "get.csv"
    c.Lang = "jp"

    await twint.run.Search(c)

def read_csv():
    csv_list = []
    with open('get.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_list.append(row.split(' '))
    return csv_list

def get_media_tweet(media_type, csv_list):
    fixed_csv_list = []
    #media_type = が1なら画像などリンク付きツイートのみ、0ならリンクなしのツイートのみ、それ以外なら全て
    if media_type == 2:
        fixed_csv_list = csv_list
    elif media_type == 1:
        for i in csv_list:
            #httpを含むものはリンク付きツイート
            if i[5].find('http') != -1:
                fixed_csv_list.append(i)
    elif media_type == 0:
        for i in csv_list:
            #httpを含まないものはリンクなしツイート
            if i[5].find('http') == -1:
                fixed_csv_list.append(i)
    return fixed_csv_list

async def get_tweet_main(twitter_username, search_word, media_type):
    await get_tweet_csv(twitter_username, search_word)
    csv_list = read_csv()
    os.remove('get.csv')
    csv_list = get_media_tweet(media_type, csv_list)
    return csv_list[0:9]
