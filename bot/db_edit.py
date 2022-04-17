import sqlite3

db_name = ''
def check_db(c):
    global db_name
    #テーブルの存在を確認
    c.execute(f"SELECT * FROM {db_name} WHERE type='table' AND name='{db_name}'")
    if c.fetchone() is None:
        print("error: can't access database file.")
        exit()
    else:
        print("database file is ready. " + str(c.fetchone()))

def create_db(DB_NAME):
    global db_name
    db_name = DB_NAME

    try:
        conn = sqlite3.connect(f'{DB_NAME}.db')
        c = conn.cursor()
        #テーブルはDBファイル名と同じ名前、レコードは識別ID、discordユーザー名、チャンネルID、ツイートID、media(boolean)、条件ワードを格納する
        c.execute(f"CREATE TABLE IF NOT EXISTS {DB_NAME}(id INTEGER PRIMARY KEY, user_name TEXT, channel_id TEXT, tweet_id TEXT, media BOOLEAN, condition_word TEXT)")
        conn.commit()
        check_db(c)
        conn.close()

    except sqlite3.OperationalError as e:
        print("please edit config.ini. " + str(e))
        exit()


