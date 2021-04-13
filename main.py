import os
from dotenv import load_dotenv


import discord
import discord_slash
from discord_slash.utils.manage_commands import create_option

from utils.responses import BotContext

# Load .env
load_dotenv()

# Commands imports
from commands.ping import ping
from commands.say import say
from commands.eight_ball import eight_ball
from commands.reddit import reddit



client = discord.Client()
slash_c = discord_slash.SlashCommand(client=client, sync_commands=True)

g = [628610131525107743, 666402364026257419]

# Slash commands
@client.event
async def on_ready():
    print('Bot is ready!')

@slash_c.slash(name="ping", description="Ping", guild_ids=g)
async def ping_command(ctx):
    await ping(BotContext(ctx)) 


@slash_c.slash(name="say", description="echo what u say", options=[
    create_option("content", "The content to echo", 3, True)
],
guild_ids=g)
async def say_command(ctx, content: str):
    await say(BotContext(ctx), content)


@slash_c.slash(name="8ball", description="What u gonna get?", options=[
    create_option("question", "What do u want to ask of the magic 8ball", 3, True)
],
guild_ids=g)
async def eight_ball_command(ctx, question: str):
    await eight_ball(BotContext(ctx), question)

@slash_c.slash(name="reddit", description="Get a random post from a subreddit", options=[
    create_option("subreddit", "Subreddit to get random post from", 3, True)
],
guild_ids=g)
async def reddit_command(ctx, sub: str):
    await reddit(BotContext(ctx), sub)


client.run(os.getenv('DISCORD_TOKEN'))