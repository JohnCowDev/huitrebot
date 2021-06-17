import discord
import os
import random

image = [
            'https://img.cuisineaz.com/660x660/2013/12/20/i15433-recette-d-huitres-au-naturel.jpeg',
            'https://s3-eu-west-1.amazonaws.com/images-ca-1-0-1-eu/recipe_photos/original/676/ouverture-huitres-3000x2000.jpg',
            'https://www.sciencesetavenir.fr/assets/img/2020/12/17/cover-r4x3w1000-5fdb83b06eec4-23698-1410138-k2-k1-3257671-jpg.jpg',
            'https://www.jeanluclegall.fr/images/Image/Huitre-La-Breizh-2.jpg'
        ]
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('huitre'):
        await message.channel.send(random.choice(image))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello there'):
        await message.channel.send('https://tenor.com/V1tn.gif')
@client.event
async def on_message(message):
    if ("chocolatine") in message.content:
        print("non pas bien")
        await message.channel.send('Pas bien {}'.format(message.author.mention))
        await message.delete()

client.run(str(input())