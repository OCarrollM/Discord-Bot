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
    
    if message.content == 'embed':
        bot_channel = client.get_channel(988388873363161128)

        myEmbed = discord.Embed(title="Current version", description="Bot version 1.0", color=0xff0000)
        myEmbed.add_field(name="Version code: ", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date released: ", value="June 21st 2022", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Morgan")

        await bot_channel.send(embed=myEmbed)



# Run client on server
client.run('')