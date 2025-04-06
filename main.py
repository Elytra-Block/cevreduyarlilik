import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$sise'):
        await message.channel.send("hmmm şişeler mii biraz düşünelim plastik mi cam mı?!")
    elif message.content.startswith("$plastik"):
        await message.channel.send("plastikler yapılması kolay fakat dünyadan yok olması zor olanlar... 500 yıll falan anlarsın ya?")
    elif message.content.startswith("$cam"):
        await message.content.startswith("hmm bak bu güzel cam şişeler iyidir!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
