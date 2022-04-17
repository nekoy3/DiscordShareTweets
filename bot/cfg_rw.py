import bot
import configparser

def main():
    config = configparser.ConfigParser()

    config['BOT'] = {
        'single_account_max_register_channel': 5,
        'checking_tweet_delay_seconds': 300,
        'bot_request_delay_seconds': 5
    }

    with open('./config.ini', 'w') as file:
        config.write(file)

if __name__ == "__main__":
    main()