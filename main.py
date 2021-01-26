import webserver

import discord
import os
import database as db

token = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messagetext = message.content.lower()

    if messagetext.startswith(['steno']):
      if hasattr(message, 'reference'):
        message.delete()
        await message.channel.send('Got it!', delete_after=5)
      else:
        deleteindex = messagetext.find("delete")
        if deleteindex != -1:
          deleteindex += 7
          word = messagetext[deleteindex:deleteindex + 4]
          db.del_entry(word)
          await message.channel.send("Successfully deleted record with word " + word.upper())
          message.delete()
          return
        await message.channel.send(
            'Don\'t know what I should do. Make sure you reply to posts you want me to record!',
            delete_after=10)
        message.delete()
        return


webserver.run_server()

client.run(token)
