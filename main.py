import discord
import os
import requests as r 
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message, url):
    if message.author == client.user:
        return
    
    endpoint = "http://alb-fast-api-model-serving-v2-1905986998.us-east-1.elb.amazonaws.com:8000/predict?url="
    #url = "https://i0.statig.com.br/bancodeimagens/3p/mx/f2/3pmxf2ta5jp03y7ug7ci16fus.jpg"

    if message.content.startswith('!pipoca' + url):
        response = r.get(endpoint + url)
        pretty_json = json.loads(response.text)
        await message.channel.send(json.dumps(pretty_json, indent=2))
    
    else:
        await message.channel.send(content=message.attachments[0].url)

client.run(os.getenv('TOKEN'))