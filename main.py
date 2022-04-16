import discord
import requests
import random

token = ''

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name + " - " + str(client.user.id))
    print("{0.user}".format(client))
    print('------')
    print('USERNAME||MESSAGE||CHANNEL||TIME')
@client.event
async def on_message(message):
    username = message.author
    user_message = str(message.content)
    channel = str(message.channel.name)
    time = str(message.created_at)
    print(f'{username} || {user_message} || {channel} || {time}')

    if message.author == client.user:
        return

    if user_message == "!help":
        await message.channel.send("Use ![pokemon] to get a pokemon's picture")

    elif user_message[0] == "!":
        salutations = ["The great and glorious ", "The mighty and powerful ", "The efficient and effective ", "The cute and cuddly ", "The fear-striking and terrifying "]
        url = "https://pokeapi.co/api/v2/pokemon/" + user_message.replace("!","") + "/"
        response = requests.get(url)
        if response.status_code == 404:
            await message.channel.send(f"'{user_message.replace('!','')}' was not found.")
            return
        elif response.status_code == 200:
            results = response.json()
            await message.channel.send(f"{random.choice(salutations)}{results['name']}:")
            await message.channel.send(results['sprites']['other']['official-artwork']['front_default'])
            return

if __name__ == "__main__":
    client.run(token)