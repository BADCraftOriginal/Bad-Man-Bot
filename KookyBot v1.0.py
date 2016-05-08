import discord
import requests
from discord.ext import commands


description = '''The Unofficial KookyCraft Discord Robot.'''
client = discord.Client()
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!twitch'):
        command = message.content()
        channel = message.content()
        if command == '!twitch followers %s' % channel:
            follows = requests.get('https://api.twitch.tv/kraken/channels/' + channel + '/follows')
            followcount = follows["_total"]
            await client.send_message(message.channel, channel, 'has', followcount, 'followers!')





client.run('token')