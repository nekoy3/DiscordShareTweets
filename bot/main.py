import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[956435214824009748])
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run("token")