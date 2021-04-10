import discord
from discord.ext import commands


client = commands.Bot(command_prefix=".")

#Testando se o bot esta online#
@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('------------')

#Imprimindo a mensagem no canal#
@client.event
async def on_message(message):
         if message.content.startswith(">ola"):
                       channel = message.channel
                       await channel.send("Pai ta on , Clã")

         if message.content.startswith(">lindo"):
                       channel = message.channel
                       await channel.send("voce meu lindo criador")

client.run() #token 