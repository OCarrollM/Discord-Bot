import discord
from discord.ext import commands
import random

description = '''Displays usage of the commands system'''

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='--', description=description, intents=intents)

# Message contents: --version
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
    # bot_channel = client.get_channel(988388873363161128)
    # await bot_channel.send('Pumpz v2 is online')

    print('logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Message contents: --add #1, #2
@client.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

# Message contents: --roll #
@client.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

# Message contents: --repeat message, #
@client.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

# Message contents: --joined @member
@client.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@client.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='client')
async def _client(ctx):
    await ctx.send('Yes, pumpz is cool')


client.run('')