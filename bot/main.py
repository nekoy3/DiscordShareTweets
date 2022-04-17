import bot
import discord

b = discord.Bot()

def main():
    global b

    @b.event
    async def on_ready():
        print(f"We have logged in as {b.user}")

    @b.slash_command(guild_ids=[956435214824009748])
    async def hello(ctx):
        await ctx.respond("Hello!")

    b.run("token")
    
    try:
        b.run('token')
    except KeyboardInterrupt:
        print("\nLogout")
        b.logout()

if __name__ == "__main__":
    main()