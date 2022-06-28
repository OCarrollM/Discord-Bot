import discord
from discord.ext import commands

# Client (Variable for bot work)
client = commands.Bot(command_prefix='--')

@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="Current version", description="Bot version 1.0", color=0xff0000)
    myEmbed.add_field(name="Version code: ", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date released: ", value="June 21st 2022", inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Morgan")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    # Code

    bot_channel = client.get_channel(988388873363161128)

    await bot_channel.send('My name is deez')

@client.event
async def on_disconnect():
        bot_channel = client.get_channel(988388873363161128)
        await bot_channel.send('Disconnected')

@client.event
async def on_message(message):
    
    if message.content == 'pumps':
        bot_channel = client.get_channel(988388873363161128)
        await bot_channel.send('pumps?!?!')

    if message.content == 'morb':
        bot_channel = client.get_channel(988388873363161128)
        await bot_channel.send('It\'s morbin time')
    
    if message.content == 'embed':
        bot_channel = client.get_channel(988388873363161128)

        myEmbed = discord.Embed(title="Current version", description="Bot version 1.0", color=0xff0000)
        myEmbed.add_field(name="Version code: ", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date released: ", value="June 21st 2022", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Morgan")

        await bot_channel.send(embed=myEmbed)

    if message.content == 'clear':
        async def clearContent(ctx, amount=100):
            channel = ctx.message.channel
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            await client.say('Messages deleted')
    
    await client.process_commands(message)

# Run client on server
client.run('')