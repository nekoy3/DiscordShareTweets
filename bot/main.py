from cfg_rw import config_settings
from get_tweet import get_tweet_main
import db_edit
import global_value as g

import discord
from discord.commands import Option
import asyncio

def get_latest_tweet_id_sync(ctx, search_word, media_type):
    tweet_list = get_tweet_main('ApexTimes', search_word, media_type)
    print(str(tweet_list))
    latest_tweet_id = tweet_list[0][0]
    #ctxでチャンネルにlatest_tweet_idを送信
    ctx.send(latest_tweet_id)

def main():
    config = config_settings()

    try:
        g.TOKEN = config['BOT']['bot_token']
        g.SET_MAX_CHANNEL_COUNT = config['BOT']['single_account_max_register_channel']
        g.CHECK_DELAY = config['BOT']['checking_tweet_delay_seconds']
        g.BOT_REQUEST_DELAY = config['BOT']['bot_request_delay_seconds']
        g.DB_NAME = config['BOT']['db_name']
        g.LIMIT_SCRAPING_DAY_COUNT = config['BOT']['limit_scraping_day_count']
    except KeyError:
        print("please edit config.ini")
        exit()
    
    db_edit.create_db(g.DB_NAME)

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
        media_type: Option(bool, 'mediaのみ(true)/以外(false)を取得するかどうかを入力してください。(両方取得する場合は引数を与えない）', required=False, default=False),
    ):
        #入力例：https://twitter.com/ApexTimes
        user_id = user_url.split('/')[-1]
        if search_word is None:
            search_word = ''

        if media_type is None:
            media_type = 2
        elif media_type is True:
            media_type = 1
        else:
            media_type = 0

        channel_id = ctx.channel.id
        latest_tweet_id = get_tweet_main(user_id, search_word, media_type)[0][0]
        db_edit.first_set_db_run(user_id, channel_id, user_id, media_type, search_word, latest_tweet_id)
        await ctx.respond(f"{user_id}を登録しました。")
    
    @d_bot.slash_command(guild_ids=[956435214824009748])
    async def test_search(
        ctx,
        search_word: Option(str, '検索ワードを入力してください。', required=False),
        media_type: Option(bool, 'mediaのみ(true)/以外(false)を取得するかどうかを入力してください。', required=False),
    ):
        await ctx.respond("please wait...")
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, get_latest_tweet_id_sync(ctx, search_word, media_type), 3)
    
    try:
        d_bot.run(g.TOKEN)
    except KeyboardInterrupt:
        print("\nLogout")
        d_bot.logout()
    

if __name__ == "__main__":
    main()