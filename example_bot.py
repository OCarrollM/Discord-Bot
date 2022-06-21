import discord

# Client (Variable for bot work)
client = discord.Client()

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

# Run client on server
client.run('OTg4Mzg5MTYxMDg0MDA2NDQw.GwfPEf.PGvVp_fKxDNTU1449HoEVUYczliT5hmYZ0gV2k')