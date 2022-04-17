from cfg_rw import config_settings
import db_edit
import discord

def main():
    config = config_settings()

    try:
        token = config['BOT']['bot_token']
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
    async def hello(ctx):
        await ctx.respond("Hello!")
    
    try:
        d_bot.run(token)
    except KeyboardInterrupt:
        print("\nLogout")
        d_bot.logout()

if __name__ == "__main__":
    main()