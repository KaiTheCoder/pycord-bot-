import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix="!") 
general_guild_id = 957923572767137825
token = 'OTU3OTIxODM4MTQ1NjIyMDQ2.YkF0Ow.z5Qk4WQgX-d5NlfReXfehsq880I'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello!")

@hello.error
async def hello_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)

bot.run(token)


