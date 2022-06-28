import discord
from discord.ext import commands

client = commands.Bot(command_prefix='--')

@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="Current version", description="Bot version 2.0", color=0xf08b3e)
    myEmbed.add_field(name="Version code: ", value="v2.0.0", inline=False)
    myEmbed.add_field(name="Date released: ", value="June 28th 2022", inline=False)
    myEmbed.set_footer(text="Improved bot mechanics")
    myEmbed.set_author(name="Morgan")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    bot_channel = client.get_channel(988388873363161128)
    await bot_channel.send('Pumpz v2 is online')

client.run('')