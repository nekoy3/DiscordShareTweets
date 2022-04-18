from cfg_rw import config_settings
import get_tweet
import db_edit

import discord
from discord.commands import Option

def main():
    config = config_settings()

    try:
        TOKEN = config['BOT']['bot_token']
        SET_MAX_CHANNEL_COUNT = config['BOT']['single_account_max_register_channel']
        CHECK_DELAY = config['BOT']['checking_tweet_delay_seconds']
        BOT_REQUEST_DELAY = config['BOT']['bot_request_delay_seconds']
        DB_NAME = config['BOT']['db_name']
    except KeyError:
        print("please edit config.ini")
        exit()
    
    db_edit.create_db(DB_NAME)

    d_bot = discord.Bot()

    @d_bot.event
    async def on_ready():
        print(f"We have logged in as {d_bot.user}")

    @d_bot.slash_command(guild_ids=[956435214824009748])
    async def ping(ctx):
        await ctx.respond(f"Pong! {round(d_bot.latency * 1000)}ms")
    
    @d_bot.slash_command(guild_ids=[956435214824009748])
    async def set_user(
        ctx,
        user_url: Option(int, '登録するTwitterユーザーのURLを入力してください。'),
        search_word: Option(str, '検索ワードを入力してください。', required=False),
        media_bool: Option(bool, 'mediaのみ(true)/以外(false)を取得するかどうかを入力してください。', required=False),
    ):
        #入力例：https://twitter.com/ApexTimes
        user_id = user_url.split('/')[-1]
        get_tweet.main(user_id, search_word, media_bool, ctx.user.id, SET_MAX_CHANNEL_COUNT )
    
    try:
        d_bot.run(TOKEN)
    except KeyboardInterrupt:
        print("\nLogout")
        d_bot.logout()

if __name__ == "__main__":
    main()