from nextcord.ext import commands
import os
from nextcord import Emoji, Intents,Message
import nextcord as d
import datetime, asyncio

intents = Intents.default()
intents.members = True

bot =commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def assignprof(ctx: commands.Context, userid: int, role_name: str):
    print(userid)

    guild = ctx.guild
    roles = await guild.fetch_roles()
    role_name_id = {}

    for role in roles:
        role_name_id[role.name] = role.id

    role = guild.get_role(role_name_id[role_name])

    for member in ctx.guild.members:
        if (member.id == userid):
            member1 = member
            break 

    print(member1, type(member1))
    await member1.add_roles(role)

@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def poll(ctx,*,message):
  emb=d.Embed(title="POLL", description=f"{message}")
  msg=await ctx.channel.send(embed=emb)
  await msg.add_reaction('1️⃣')
  await msg.add_reaction('2️⃣')
  await msg.add_reaction('3️⃣')
  await msg.add_reaction('4️⃣')

@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def pin(ctx,msgId:int):
  msg_to_pin = await ctx.fetch_message(msgId)
  print(msgId)
  await msg_to_pin.add_reaction("📌")
  await msg_to_pin.pin()

@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def deadline(ctx,*,message):
  now=datetime.datetime.now()
  days=int(f"{message[0:2]}")
  HOUR=int(f"{message[2:4]}")
  MIN=int(f"{message[4:6]}")
  channel=bot.get_channel(972271682834272399)
  await ctx.channel.send("DEADLINE in "+str(days)+" Days at "+str(HOUR+1)+":"+str(MIN))
  then=now.replace(hour=HOUR, minute=MIN)
  wait=(then-now).total_seconds()
  await asyncio.sleep(wait)
  await ctx.channel.send("ONE HOUR LEFT TILL DEADLINE!")



@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def Create_Role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def create_TC(ctx,channel_name):
  guild=ctx.guild
  text_channel_list = []
  for guild in bot.guilds:
    for channel in guild.text_channels:
      text_channel_list.append(channel.name)
  if channel_name in text_channel_list:
    await ctx.send(f"Channel {channel_name} already exists")
  else:
    mbed=d.Embed(
      title='Success',
      description="{} has been successfully Created.".format(channel_name)
    )
    await guild.create_text_channel(name=channel_name)
    await ctx.send(embed=mbed)

@bot.command()
@commands.check_any(commands.has_permissions(administrator=True), commands.has_role("prof"))
async def delete_TC(ctx,channel:d.TextChannel):
  mbed=d.Embed(
    title='Success',
    description=f"{channel} has been deleted."

  )
  await ctx.send(embed=mbed)
  await channel.delete()


TOKEN = os.environ.get('TOKEN')

bot.run(TOKEN)

