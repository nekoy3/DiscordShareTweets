from get_tweet import get_tweet_main
import global_value as g

import sqlite3

db_name = ''
def check_db(c):
    global db_name
    #テーブルの存在を確認
    c.execute("select name from sqlite_master where type='table'")
    for i in c.fetchall():
        table_name = i[0]
        break

    if table_name == 'tweet_share':
        print(f"{db_name} is already exist.")
        return
    else:
        print("error: can't access database table.")
        exit()

def create_db(DB_NAME):
    global db_name
    db_name = DB_NAME

    try:
        conn = sqlite3.connect(f'{DB_NAME}.db')
        c = conn.cursor()
        #テーブルはtweet_share、レコードは識別ID、discordユーザー名、チャンネルID、Twitter共有ユーザーID、media(boolean)、条件ワード、最後に取得したツイートidを格納する
        c.execute(f"CREATE TABLE IF NOT EXISTS tweet_share(id INTEGER PRIMARY KEY, discord_user_id TEXT, channel_id TEXT, twitter_user_id TEXT, media BOOLEAN, condition_word TEXT, latest_tweet_id TEXT)")
        conn.commit()
        check_db(c)
        conn.close()

    except sqlite3.OperationalError as e:
        print("please edit config.ini. " + str(e))
        exit()

def run_sql(sql_text):
    conn = sqlite3.connect(f'{db_name}.db')
    c = conn.cursor()
    check_db(c)
    c.execute(sql_text)
    conn.commit()
    conn.close()
    return c.fetchall()

def first_set_db_run(user_id, channel_id, twitter_user_id, media, condition_word, latest_tweet_id):
    sql_text = f"INSERT INTO tweet_share(discord_user_id, channel_id, twitter_user_id, media, condition_word, latest_tweet_id) VALUES('{user_id}', '{channel_id}', '{twitter_user_id}', {media}, '{condition_word}', '{latest_tweet_id}')"
    run_sql(sql_text)

    #ツイートを最新の一つのみ取得する(get_tweet.py)
    tweet_csv = get_tweet_main(twitter_user_id, condition_word, latest_tweet_id, g.LIMIT_SCRAPING_DAY_COUNT)