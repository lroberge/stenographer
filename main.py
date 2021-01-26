import webserver

import discord
import os

token = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if hasattr(message, 'reference'):
        await message.channel.send(
            'Don\'t know what message I should record. Make sure you reply to it!',
            delete_after=10)
        message.delete()
        return

    if message.content.lower().startswith(['steno']):
        await message.channel.send('Got it!', delete_after=5)
        message.delete()
        return


webserver.run_server()

client.run(token)
