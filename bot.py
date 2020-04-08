import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '?')
client.remove_command('help')
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = "welcome")
    welcome_msg = "ALERT"
    embed = discord.Embed(title=str(welcome_msg), description="{0} Has Joined Our Server, Don't Be Shy And Join The Party Lad".format(member.mention), color=0xFF69B4)
    await channel.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name ="Members")
    await member.add_roles(role)
    embed = discord.Embed(title="{}'s info".format(member.name), description="Test", color=0xFF69B4)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Roles", value=member.top_role)
    embed.add_field(name="Joined", value=member.joined_at)
    embed.add_field(name="Created", value=member.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    channel = discord.utils.get(member.guild.channels, name = "info")
    await channel.send(embed=embed)
@client.event
async def on_ready():
    print('Bot is ready.')
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
@commands.has_role("Amats")
async def clear(ctx, amount=0):
   if amount == "all":
        amount = 5000
        await ctx.channel.purge(limit=amount)
        embed =  discord.Embed(title='Cleaning',description = 'You have cleared everything', color=0xFF69B4)
        await ctx.send(embed=embed)
        return amount
        
   if amount == 0:
       embed = discord.Embed(title='Fail',description='Please specify how many messages you wanna delete', color=0xFF69B4)
       await ctx.send(embed=embed)
       return amount
    
   deleted =  await ctx.channel.purge(limit=amount)
   embed = discord.Embed(title='Cleaning',description = 'Deleted {} message(s)'.format(len(deleted)), color=0xFF69B4)
   await ctx.send(embed=embed)

@client.command()
async def heh(ctx):
    await ctx.send('Shutup Lux')
@client.command()
@commands.has_role("Amats")
async def ban(ctx, user: discord.Member='None'):
    embed = discord.Embed(title="Oh Shit 0_0", description="{0} got banned from the server".format(user.name), color=0xFF69B4)
    if not user:
        embed = discord.Embed(title='Fail',description='Please specify a user', color=0xFF69B4)
        ctx.send(embed=embed)
        return
    await user.ban()
    await ctx.send(embed=embed)
@client.command()
@commands.has_role("Amats")
async def kick(ctx, user: discord.Member=None):
    embed = discord.Embed(title="Bye Bye :wave:", description="{} got kicked from the server".format(user), color=0xFF69B4)
    if not user:
        embed = discord.Embed(title='Fail',description='Please specify a user', color=0xFF69B4)
        ctx.send(embed=embed)
        return
    await user.kick()
    await ctx.send(embed=embed)
@client.command()
@commands.has_role("Amats")
async def jail(ctx, user: discord.Member=None):
    role = discord.utils.get(user.guild.roles, name='Jail')
    role2 = discord.utils.get(user.guild.roles, name='Members')
    embed = discord.Embed(title="Jail time baby!!", description="{0} Has been Jailed.".format(user.name), color=0xFF69B4)
    if not user:
        embed = discord.Embed(title='Fail',description='Please specify a user', color=0xFF69B4)
        await ctx.send(embed=embed)
        return
    await user.add_roles(role)
    await user.remove_roles(role2)
    await ctx.send(embed=embed)
@client.command()
@commands.has_role("Amats")
async def unjail(ctx, user: discord.Member=None):
    role = discord.utils.get(user.guild.roles, name ="Jail")
    role2 = discord.utils.get(user.guild.roles, name ="Members")
    embed = discord.Embed(title="Fly birdy!", description="{} here ya go my love, you are free to go >.<".format(user), color=0xFF69B4)
    if not user:
        embed = discord.Embed(title='Fail',description='Please specify a user', color=0xFF69B4)
        await ctx.send(embed=embed)
        return
    await user.remove_roles(role)
    await user.add_roles(role2)
    await ctx.send(embed=embed)
@client.command()
async def creds(ctx):
    embed = discord.Embed(title="Credits", description="A very huge applause to Luxunator ", color=0xFF69B4)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx, entity=client):
        msg= f'┌━━━━━━━━[General Commands]━━━━━━━━\n' \
        f'╰[?help]━[Shows Bot Help Menu]\n' \
          f'' \
          f'┌━━━━━━━━[Mod Commands]━━━━━━━━\n' \
          f'╰[?clear (#_of_messages)]━[Deletes the last # of messages in the channel]\n' \
          f'╰[?kick @member]━[Kicks member from server]\n' \
          f'╰[?ban @member]━[Bans member from server]\n' \
          f'╰[?jail @member]━[Sends member to #jail until unjailed]\n' \
          f'╰[?unjail @member]━[Unjails member and lets them talk in other channels again]\n' \
        f'╰[?creds ]━[THE ONE ]\n'\
        f'╰[?clearall ]━[Deletes all the messages in the channel ]\n'
        embed = discord.Embed(title='Test Help Menu ＼(≧▽≦)／', description=msg, color=0xFF69B4)
        await ctx.send(embed=embed)

@client.command()
async def clearall(ctx, amount=5000):
        await ctx.channel.purge(limit=amount)
        embed =  discord.Embed(title='Cleaning',description = 'You have cleared everything', color=0xFF69B4)
        await ctx.send(embed=embed)
        return amount

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(title='Unbanned',description = 'Congratulations, you have been unbanned {}'.format(user.mention), color=0xFF69B4)
            await ctx.send(embed=embed)

            



client.run('ENTER KEY HERE')

