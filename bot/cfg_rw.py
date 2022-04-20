import configparser
import os

def create_config():
    config = configparser.ConfigParser()

    config['BOT'] = {
        'single_account_max_register_channel': 5,
        'checking_tweet_delay_seconds': 300,
        'bot_request_delay_seconds': 5,
        'bot_token': '',
        'db_name': 'tweet_share_db',
        'limit_scraping_day_count': 5
    }

    with open('./config.ini', 'w') as file:
        config.write(file)

def get_config():
    
    config = configparser.ConfigParser()
    config.read('./config.ini')
    return config

def config_settings():

    if not os.path.exists('./config.ini'):
        create_config()
        print("please edit config.ini")
        exit()

    else:
        print("reading config file.")
        config = get_config()
        return config

if __name__ == "__main__":
    config_settings()