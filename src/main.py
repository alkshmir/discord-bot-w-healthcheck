import os
import discord 
import healthcheck

class CustomClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hc = healthcheck.healthcheck(self, 8080)

    async def on_ready(self):
        print('Logged in as {}. user_id={}'.format(self.user.name,self.user.id))
        print('-'*20)

    async def on_message(self,message):
        if message.author == self.user:
            return
        print(message.content)
        await message.channel.send("foo")

if __name__ == "__main__":
        
    cc = CustomClient()
    cc.run(os.environ.get('ENV_VAR_DISCORD_ID'))