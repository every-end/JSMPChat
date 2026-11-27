import discord
import asyncio
import random
import os
from discord.ext import commands

# JSMP Bot version 0.61.1

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("Discord token not found! Check your .env file.")

# Bot prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Bot is online message
ONLINE_CHANNEL_ID = 1408882996609548362
startup_message_sent = False

@bot.event
async def on_ready():
    global startup_message_sent

    # Bot status
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("!commandlist | JSMP Bot version 0.61.1")
    )

    print(f"Bot is online: {bot.user}")

    # Prevent duplicate startup messages
    if startup_message_sent:
        return

    channel = bot.get_channel(ONLINE_CHANNEL_ID)

    if channel is None:
        try:
            channel = await bot.fetch_channel(ONLINE_CHANNEL_ID)
        except discord.HTTPException as error:
            print(f"Could not find channel: {error}")
            return

    # Check that the channel supports sending messages
    if not isinstance(channel, (discord.TextChannel, discord.Thread)):
        print("ERROR: The selected ID is not a text channel or thread!")
        return

    try:
        await channel.send(
            "JSMP bot is now online. Do ``!commandlist`` to see available commands.\n"
        )

        startup_message_sent = True
        print("Online notification sent successfully!")

    except discord.Forbidden:
        print("ERROR: Missing permissions to send messages!")

    except discord.HTTPException as error:
        print(f"Discord API Error: {error}")

FACTIONS = [
    {
        "name": "J-Guards",
        "flag": "https://cdn.discordapp.com/attachments/1563602052096204970/1563914980128981143/Titelloses_347_20261025144708.png?ex=6afd0693&is=6afbb513&hm=da3fb32f1cab0c08e31c08360e1f6b51e178710161626f7f0abef80b9e2d1d1c&",
        "description": "A faction situated far away in the greenery of the Overworld. Just some lt1 dudes that kill trespassers on sight.",
        "members": ["JupiterianGuy", "Every end", "Rayo", "Kiki", "Moon", "Star"],
        "color": discord.Color.yellow()
    },
    {
        "name": "Le assassins",
        "flag": "https://cdn.discordapp.com/attachments/1563602052096204970/1571958243834728468/Untitled19_20261116184015.png?ex=6afd4872&is=6afbf6f2&hm=fc679f8b094c2fa8a4ff91d94ae4220d25c2ebdc6467e5a3e022b8c032439858&",
        "description": "idk man prob hitmans",
        "members": ["1Temy", "Hoof"],
        "color": discord.Color.red()
    }
]

# Minecraft server information
SERVER_IP = "jupismp.mcsh.gg"
SERVER_VERSION = "1.9 to 26.3"

# !serverip command
@bot.command()
async def serverip(ctx):
    embed = discord.Embed(
        title="Server Information",
        description="Welcome to JSMP!",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Server IP",
        value=SERVER_IP,
        inline=False
    )

    embed.add_field(
        name="Version",
        value=SERVER_VERSION,
        inline=True
    )

    embed.add_field(
        name="Platform",
        value="Java + Bedrock Edition",
        inline=True
    )

    embed.add_field(
        name="Port",
        value="19132",
        inline=True
    )

    embed.set_footer(text="Thanks for playing!")

    await ctx.send(embed=embed)

# !staff command
@bot.command()
async def staff(ctx):
    await ctx.send("Trial Moderator (Stage 1) role has been given to you! Make sure to use your powers carefully to get promoted.")
    
# !sarix command
@bot.command()
async def sarix(ctx):
    await ctx.send("No matter how hard the next top 1 demon will be, people can make the same thing, but extended and this exactly why, we always get new hardest levels in Geometry Dash, the only condition is that someone is willing to verify it."
"-Sarix")

# !nuke command
@bot.command()
async def nuke(ctx):
    messages = ["Nuking Jupiterian Community...", "25%...", "50%...", "75%...", "100%! Channels Deleted, Roles Deleted, Server Nuked!"]

    for message in messages:
        await ctx.send(message)
        await asyncio.sleep(2)

# !doxx command
@bot.command()
async def doxx(ctx):
    messages = ["Bypassing firewall...", "Disabling Antivirus...", "Accessing personal information...", "Done! User has been captured!"]

    message = await ctx.send(messages[0])

    for text in messages[1:]:
        await asyncio.sleep(2)
        await message.edit(content=text)

# !ping command
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! 🏓 {latency}ms")

# !say command
@bot.command()
async def say(ctx, *, text):
    await ctx.send(
        text,
        allowed_mentions=discord.AllowedMentions.none()
    )

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])

    embed = discord.Embed(
        title="🪙 Coinflip",
        description=f"The coin landed on **{result}!**",
        color=discord.Color.gold()
    )

    embed.set_footer(text=f"Flipped by {ctx.author.display_name}")

    await ctx.send(embed=embed)

# !commandlist command
@bot.command()
async def commandlist(ctx):
    embed = discord.Embed(
        title="Available Commands",
        description="Here are the bot commands:",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="!serverip",
        value="Shows the Minecraft server IP.",
        inline=False
    )

    embed.add_field(
        name="!ping",
        value="Checks bot latency.",
        inline=False
    )

    embed.add_field(
        name="!commandlist",
        value="Displays this command list.",
        inline=False
    )

    embed.add_field(
        name="!nuke",
        value="Nukes the server. (joke command)",
        inline=False
    )

    embed.add_field(
        name="!doxx <user>",
        value="Doxxes people. (joke command)",
        inline=False
    )

    embed.add_field(
        name="!staff",
        value="Gives you staff. (joke command)",
        inline=False
    )

    embed.add_field(
        name="!owner",
        value="Tries to give you owner but jupi might catch you. (joke command)",
        inline=False
    )

    embed.add_field(
        name="!say <word>",
        value="Copies exactly what you say. (It can't mention people.)",
        inline=False
    )

    embed.add_field(
        name="!factions",
        value="Shows the list of factions in JSMP.",
        inline=False
    )

    embed.add_field(
        name="!faction <faction name>",
        value="Shows information about a faction.",
        inline=False
    )
    
    embed.add_field(
        name="!sarix",
        value="Ronaldo pasta wanted me to add this it does nothing other than showing a quote.",
        inline=False
    )

    embed.add_field(
        name="!coinflip",
        value="Flips a coin.",
         inline=False
    )
    
    await ctx.send(embed=embed)

# !owner command
@bot.command()
async def owner(ctx):
    await ctx.send("WARNING, SOMEONE HAS ATTEMPTED TO GET OWNER IN THIS SERVER. SENDING A DM TO JUPI 🚨")
        
# faction command
@bot.command()
async def faction(ctx, *, name=None):

    if not name:
        await ctx.send(
            "❌ Usage: `!faction <faction name>`"
        )
        return

    # Find the requested faction
    selected = None

    for f in FACTIONS:
        if f["name"].lower() == name.lower():
            selected = f
            break

    # Check if faction exists
    if selected is None:
        await ctx.send(
            f"❌ Faction `{name}` not found!"
        )
        return

    # Create faction embed
    embed = discord.Embed(
        title=f"{selected['name']}",
        description=selected["description"],
        color=selected["color"]
    )

    embed.add_field(
        name="Members",
        value=", ".join(selected["members"]) or "No members",
        inline=False
    )

    embed.add_field(
        name="Member Count",
        value=str(len(selected["members"])),
        inline=True
    )

    embed.set_image(url=selected["flag"])

    embed.set_footer(
        text="JSMP Faction Directory"
    )

    await ctx.send(embed=embed)

@bot.command()
async def factions(ctx):

    embed = discord.Embed(
        title="JSMP Faction List",
        description=(
            "Here are all the factions in our SMP!\n\n"
            "Use `!faction <name>` to view faction information."
        ),
        color=discord.Color.gold()
    )

    # Create the faction text
    faction_text = ""

    for faction in FACTIONS:
        faction_text += f"**{faction['name']}**\n"

    # Add faction names and total count
    embed.add_field(
        name=f"Available Factions ({len(FACTIONS)})",
        value=faction_text or "No factions available.",
        inline=False
    )

    embed.set_footer(text="JSMP Faction Directory")

    await ctx.send(embed=embed)

bot.run(TOKEN)
