# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

from logic_poke import Pokemon
import requests
import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')

@bot.command()
async def rawr(ctx):
    await ctx.send("RAWR")
    await ctx.send("you found an easter egg!")

@bot.command()
async def miau(ctx):
    await ctx.send("https://youtu.be/AkufJdMjnyU?si=FzcqJQuotfsJJZ_Q")
    await ctx.send("you found an easter egg!")

@bot.command()
async def aboutblank(ctx):
    await ctx.send("about:blank")
    await ctx.send("you found an easter egg!")

@bot.command()
async def brotha(ctx):
    await ctx.send("https://www.youtube.com/watch?v=wLg04uu2j2o")
    await ctx.send("you found an easter egg!")

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)

# The '$go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    # if author not in Pokemon.pokemons.keys():
    pokemon = Pokemon(author)  # Creating a new Pokémon
    await ctx.send(await pokemon.info())  # Sending information about the Pokémon
    image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
    if image_url:
        embed = discord.Embed()  # Creating an embed message
        embed.set_image(url=image_url)  # Setting up the Pokémon's image
        await ctx.send(embed=embed)  # Sending an embedded message with an image
    else:
        await ctx.send("Failed to upload an image of the pokémon.")

@bot.command()
async def multiply(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def by(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left ** right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# overwriting kalimat.txt
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)

# random local meme image
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animeme(ctx):
    img_name = random.choice(os.listdir('tnbg'))
    with open(f'tnbg/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)


# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

@bot.command()
async def sos(ctx):
    await ctx.send(f'if you need help, contact nownotnow2000@proton.me, this bot is (mostly) not my code')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# @bot.command()
# async def mem(ctx):
#     # try by your self 2 min
#     img_name = random.choice(os.listdir('images'))
#     with open(f'images/{img_name}', 'rb') as f:
#         picture = discord.File(f)
 
#     await ctx.send(file=picture)

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here


bot.run('LaLaLALAlAl12LAlAlAlla')
