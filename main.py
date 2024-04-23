import discord
from yaml import safe_load
from pathlib import Path

## Stocking the token in a file config.yml where (token:"Yourtoken")
config = safe_load(Path("config.yml").read_text())
token = config["token"]

class bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print("-------------------------")

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('!hello'):
            await message.reply('Hello!', mention_author=True)
        await self.nb_user(message)
        await self.joindate(message)

  #Return the number of users in the guild (!nb -> return the count of all the users // !nbstatus -> return the number of connected users)
    async def nb_user(self,message):
        guild = self.get_guild(#guildid)
        user_number = guild.member_count
        members = guild.members
        nb_online = 0
        if message.content == '!nb':
            await message.reply(f"Il y a {user_number} personnes sur le Discord")
        elif message.content == '!nbstatus':
            for member in members :
                if str(member.status) == 'online' or str(member.status) == 'dnd' or str(member.status) == 'idle':
                    nb_online +=1
            await message.reply(f"Il y a {nb_online} membres en ligne")
#Return the date when the user join the discord, command = !joindate
    async def joindate(self,message):
        channel = self.get_channel(#channelid)
        if message.content == '!joindate':
            user = message.author
            datejoin = str(user.joined_at)
            datejoin = datejoin[:10]
            await channel.send(f"You are a member of this discord since {datejoin}")
                    
#intents (i put all but it's better if you manage the good rights)
intents = discord.Intents.all()
client = bot(intents=intents)
client.run(token)
