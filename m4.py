import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return


    if message.content.lower() == '!ping':
        await message.channel.send('Pong!')

    if message.content.lower() == '!ajuda':
        await message.channel.send(
            '**Comandos disponíveis:*'
            '`!ping` - Responde Pong!'
            '`!ajuda` - Mostra os comandos disponíveis'
        )

    # Quando o bot for mencionado
    if client.user.mentioned_in(message):
        await message.channel.send('Oi! Você me chamou?')
