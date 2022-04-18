from db_edit import run_sql

import twint
import csv

SET_MAX_CHANNEL_COUNT_GLOBAL = 0

def set_db_fields(twitter_username, serch_word, media_bool, discord_user_id):
    global SET_MAX_CHANNEL_COUNT_GLOBAL
    #insertする前に、SET_MAX_CHANNEL_COUNTとfieldの数を比較する
    sql_text = f"SELECT * FROM tweet_share WHERE discord_user_id = '{discord_user_id}'"
    result = run_sql(sql_text)

    sql_text = f"INSERT INTO tweet_share(user_name, channel_id, twitter_user_id, media, condition_word, latest_tweet_id) VALUES('{twitter_username}', '{discord_user_id}', '{twitter_username}', {media_bool}, '{serch_word}', '{csv_list[0][0]}')"
    run_sql(sql_text)

def get_tweet_csv(twitter_username, serch_word):
    c = twint.Config()
    c.Username = twitter_username
    c.Search = serch_word
    c.Limit = 1
    c.Output = "get.csv"
    c.Lang = "jp"

    twint.run.Search(c)

def read_csv():
    csv_list = []
    with open('get.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_list.append(row.split(' '))
    return csv_list

def main(twitter_username, serch_word, media_bool, discord_user_id, SET_MAX_CHANNEL_COUNT):
    global SET_MAX_CHANNEL_COUNT_GLOBAL
    SET_MAX_CHANNEL_COUNT_GLOBAL = SET_MAX_CHANNEL_COUNT
    set_db_fields(twitter_username, serch_word, media_bool, discord_user_id)
    get_tweet_csv(twitter_username, serch_word)
    csv_list = read_csv()


if __name__ == "__main__":
    main()