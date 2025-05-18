# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

#sng = me and me = sng

from logic_poke import Pokemon
import requests
import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass
from detect_objects import detect
from model import get_class

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

yummyeyes = "i see the eyes"
dood = 2648
q = ""
hdeath = 0

IsGameStarted = 0
HguessWord = []

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

@bot.command()
async def rockpaperscissors(ctx, hand):
    hands = ["rock", "paper", "scissors"]
    machine = random.choice(hands)
    phand = hand.lower()
    await ctx.send(machine)
    if machine == phand:
        await ctx.send("tie")
    elif (machine == "rock" and phand == "paper") or (machine == "paper" and phand == "scissors") or (machine == "scissors" and phand == "rock"):
        await ctx.send("you win W")
    elif (phand == "rock" and machine == "paper") or (phand == "paper" and machine == "scissors") or (phand == "scissors" and machine == "rock"):
        await ctx.send("you lose L")
    else:
        await ctx.send("ooie gooie, you need to pick rock, paper or scissors you silly mongoose")
    
@bot.command()
async def hangman(ctx):
    global IsGameStarted
    global HguessWord
    global guessword
    if IsGameStarted != 1:
        words = ["name", "discord", "superb", "pneumonoultramicroscopicsilicovolcanoconiosis", "Methionylglutaminylarginyltyrosylglutamylserylleucylphenylalanylvalylprolylphenylalanylvalylthreonylleucylglycylaspartylprolylglycylisoleucylglutamylglutaminylserylleucyllysylisoleucylaspartylthreonylleucylisoleucylglutamylalanylglycylalanylaspartylalanylleucylglutamylleucylglycylisoleucylprolylphenylalanylserylaspartylprolylleucylalanylaspartylglycylprolylthreonylisoleucylglutaminylasparaginylalanylthreonylleucylarginylalanylphenylalanylalanylalanylglycylvalylthreonylprolylalanylglutaminylcysteinylphenylalanylglutamylmethionylleucylalanylleucylisoleucylarginylglutaminyllysylhistidylprolylthreonylisoleucylprolylisoleucylglycylleucylleucylmethionyltyrosylalanylasparaginylleucylvalylphenylalanylasparaginyllysylglycylisoleucylaspartylglutamylphenylalanyltyrosylalanylglutaminylcysteinylglutamyllysylvalylglycylvalylaspartylserylvalylleucylvalylalanylaspartylvalylprolylvalylglutaminylglutamylserylalanylprolylphenylalanylarginylglutaminylalanylalanylleucylarginylhistidylasparaginylvalylalanylprolylisoleucylphenylalanylisoleucylcysteinylprolylprolylaspartylalanylaspartylaspartylaspartylleucylleucylarginylglutaminylisoleucylalanylseryltyrosylglycylarginylglycyltyrosylthreonyltyrosylleucylleucylserylarginylalanylglycylvalylthreonylglycylalanylglutamylasparaginylarginylalanylalanylleucylprolylleucylasparaginylhistidylleucylvalylalanyllysylleucyllysylglutamyltyrosylasparaginylalanylalanylprolylprolylleucylglutaminylglycylphenylalanylglycylisoleucylserylalanylprolylaspartylglutaminylvalyllysylalanylalanylisoleucylaspartylalanylglycylalanylalanylglycylalanylisoleucylserylglycylserylalanylisoleucylvalyllysylisoleucylisoleucylglutamylglutaminylhistidylasparaginylisoleucylglutamylprolylglutamyllysylmethionylleucylalanylalanylleucyllysylvalylphenylalanylvalylglutaminylprolylmethionyllysylalanylalanylthreonylarginylacetylseryltyrosylserylisoleucylthreonylserylprolylserylglutaminylphenylalanylvalylphenylalanylleucylserylserylvalyltryptophylalanylaspartylprolylisoleucylglutamylleucylleucylasparaginylvalylcysteinylthreonylserylserylleucylglycylasparaginylglutaminylphenylalanylglutaminylthreonylglutaminylglutaminylalanylarginylthreonylthreonylglutaminylvalylglutaminylglutaminylphenylalanylserylglutaminylvalyltryptophyllysylprolylphenylalanylprolylglutaminylserylthreonylvalylarginylphenylalanylprolylglycylaspartylvalyltyrosyllysylvalyltyrosylarginyltyrosylasparaginylalanylvalylleucylaspartylprolylleucylisoleucylthreonylalanylleucylleucylglycylthreonylphenylalanylaspartylthreonylarginylasparaginylarginylisoleucylisoleucylglutamylvalylglutamylasparaginylglutaminylglutaminylserylprolylthreonylthreonylalanylglutamylthreonylleucylaspartylalanylthreonylarginylarginylvalylaspartylaspartylalanylthreonylvalylalanylisoleucylarginylserylalanylasparaginylisoleucylasparaginylleucylvalylasparaginylglutamylleucylvalylarginylglycylthreonylglycylleucyltyrosylasparaginylglutaminylasparaginylthreonylphenylalanylglutamylserylmethionylserylglycylleucylvalyltryptophylthreonylserylalanylprolylalanyltitinmethionylglutaminylarginyltyrosylglutamylserylleucylphenylalanylalanylisoleucylcysteinylprolylprolylaspartylalanylaspartylaspartylaspartylleucylleucylarginylglutaminylisoleucylalanylseryltyrosylglycylarginylglycyltyrosylthreonyltyrosylleucylleucylserylarginylalanylglycylvalylthreonylglycylalanylglutamylasparaginylarginylalanylalanylleucylprolylleucylasparaginylhistidylleucylvalylalanyllysylleucyllysylglutamyltyrosylasparaginylalanylalanylprolylprolylleucylglutaminylglycylphenylalanylglycylisoleucylserylalanylprolylaspartylglutaminylvalyllysylalanylalanylisoleucylaspartylalanylglycylalanylalanylglycylalanylisoleucylserylglycylserylalanylisoleucylvalyllysylisoleucylisoleucylglutamylglutaminylhistidylasparaginylisoleucylglutamylprolylglutamyllysylmethionylleucylalanylalanylleucyllysylvalylphenylalanylvalylglutaminylprolylmethionyllysylalanylalanylthreonylarginylacetylseryltyrosylserylisoleucylthreonylserylprolylserylglutaminylphenylalanylvalylphenylalanylleucylserylserylvalyltryptophylalanylaspartylprolylisoleucylglutamylleucylleucylasparaginylvalylcysteinylthreonylserylserylleucylglycylasparaginylglutaminylphenylalanylglutaminylthreonylglutaminylglutaminylalanylarginylthreonylthreonylglutaminylvalylglutaminylglutaminylphenylalanylserylglutaminylvalyltryptophyllysylprolylphenylalanylprolylglutaminylserylthreonylvalylarginylphenylalanylprolylglycylaspartylvalyltyrosyllysylvalyltyrosylarginyltyrosylasparaginylalanylvalylleucylaspartylprolylleucylisoleucylthreonylalanylleucylleucylglycylthreonylphenylalanylaspartylthreonylarginylasparaginylarginylisoleucylisoleucylglutamylvalylglutamylasparaginylglutaminylglutaminylserylprolylthreonylthreonylalanylglutamylthreonylleucylaspartylalanylthreonylarginylarginylvalylaspartylaspartylalanylthreonylvalylalanylisoleucylarginylserylalanylasparaginylisoleucylasparaginylleucylvalylasparaginylglutamylleucylvalylarginylglycylthreonylglycylleucyltyrosylasparaginylglutaminylasparaginylthreonylphenylalanylglutamylserylmethionylserylglycylleucylvalyltryptophylthreonylserylalanylproly",
                "dragon", "castle", "forest", "wizard", "knight", "treasure", "crown", "shield", "sword", "princess", "planet", "galaxy", "asteroid", "comet", "rocket", "nebula", "eclipse", "satellite", "gravity", "orbit", "butterfly", "beetle", "spider", "ant", "bee", "worm", "fly", "mosquito", "cricket", "caterpillar", "desert", "island", "mountain", "valley", "plateau", "canyon", "volcano", "prairie", "jungle", "tundra", "coffee", "tea", "milk", "juice", "water", "soda", "lemonade", "smoothie", "hotdog", "popcorn", "helmet", "gloves", "boots", "jacket", "scarf", "umbrella", "goggles", "backpack", "hat", "sunglasses", "violin", "piano", "guitar", "flute", "drums", "trumpet", "harp", "banjo", "cello", "saxophone", "hammer", "screwdriver", "wrench", "pliers", "drill", "saw", "ladder", "tape", "nails", "level",
                "apple", "banana", "cherry", "grape", "orange", "peach", "plum", "melon", "kiwi", "mango", "table", "chair", "sofa", "desk", "lamp", "shelf", "bed", "couch", "stool", "drawer", "ocean", "river", "lake", "pond", "stream", "waterfall", "bay", "sea", "fjord", "lagoon", "happy", "sad", "angry", "excited", "bored", "tired", "scared", "nervous", "calm", "confused", "train", "plane", "car", "bus", "bike", "boat", "ship", "subway", "tram", "scooter", "pizza", "burger", "pasta", "salad", "soup", "steak", "sandwich", "taco", "sushi", "noodle", "cloud", "rain", "snow", "storm", "wind", "sun", "fog", "hail", "lightning", "thunder", "dog", "cat", "bird", "fish", "horse", "rabbit", "mouse", "snake", "turtle", "frog", "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white", "book", "pen", "paper", "pencil", "eraser", "marker", "notebook", "folder", "ruler", "scissors",
                "jungle", "tundra", "savanna", "meadow", "cave", "cliff", "reef", "delta", "fjord", "canyon", "lantern", "candle", "torch", "mirror", "clock", "vase", "radio", "pillow", "curtain", "carpet", "gorilla", "koala", "panda", "otter", "walrus", "dolphin", "eagle", "owl", "bat", "fox", "volcano", "earthquake", "hurricane", "tsunami", "avalanche", "blizzard", "drought", "flood", "whirlpool", "cyclone", "quartz", "emerald", "diamond", "ruby", "sapphire", "topaz", "opal", "garnet", "jade", "amber", "wizard", "witch", "sorcerer", "fairy", "elf", "troll", "ogre", "dragon", "phoenix", "unicorn", "rocket", "spaceship", "satellite", "planet", "asteroid", "meteor", "galaxy", "cosmos", "nebula", "orbit", "laptop", "keyboard", "mouse", "monitor", "printer", "headphones", "microphone", "camera", "tablet", "charger", "soccer", "baseball", "cricket", "tennis", "badminton", "volleyball", "rugby", "hockey", "chess", "bowling", "violin", "guitar", "piano", "trumpet", "flute", "drums", "harp", "banjo", "cello", "clarinet"]
        await ctx.send("Welcome to hangman.")
        await ctx.send("Guess the letters in the word")
        await ctx.send("and guess the word once you know it")
        await ctx.send("You have 10 tries before the man hangs i guess")
        await ctx.send("use the command:")
        await ctx.send("hguess + your guess letter (ONLY ONE)")
        await ctx.send("to guess")
        guessword = random.choice(words)
        IsGameStarted = 1
        HguessWord = ['?'] * len(guessword)
        print(guessword)
    else:
        await ctx.send("A game is in progress")


@bot.command()
async def hguess(ctx, letter: str):
    global IsGameStarted
    global HguessWord
    global guessword
    global hdeath
    if IsGameStarted == 1:
        await ctx.send(letter)
        for i in range(len(guessword)):
            if letter in guessword[i]:
                HguessWord[i] = letter
                joined = "".join(HguessWord)
                await ctx.send(f"Correct, Currently, the Word is {joined}")
        if letter not in guessword:
            joined = "".join(HguessWord)
            await ctx.send(f"No letter in word, Currently, the Word is {joined}")
            nameme = "you have ", (6 - hdeath), "tries"
            await ctx.send(nameme)
            if hdeath == 1:
                await ctx.send("the man now has his head D:")
            elif hdeath == 2:
               await ctx.send("the man now has his head and body")
            elif hdeath == 3:
                await ctx.send("the man now has his head, body and right arm")                    
            elif hdeath == 4:
                await ctx.send("the man now has his head, body, and arms")
            elif hdeath == 5:
                await ctx.send("the man now has his head, body, arms, and legs")
            elif hdeath == 6:
                await ctx.send("THE MAN IS DEAD, YOU KILLED HIM, YOU MONSTER!, oh, also the word is ", guessword)

    elif IsGameStarted == 0:
        print("nah")
        await ctx.send("start a game of hangman first")

@bot.command()
async def climatrivia(ctx):
    global dood
    global q
    await ctx.send("Welcome to Climate Trivia!")
    await ctx.send("Answer questions if you are smart, BET.")
    questions = {
        "Which year was the hottest recorded on Earth? 1. 2024, 2. 2024, 3. 2016": 4,
        "Is climate change different from global warming? 1. Yes, 2. No": 1,
        "Is Leggeiy a cool guy? 1. Yes, 2. No, 3. Maybe": 1,
        "What percentage of global greenhouse gas emissions come from deforestation? 1. 10%, 2. 20%, 3. 30%": 2,
        "Which of these natural disasters has increased due to climate change? 1. Hurricanes, 2. Earthquakes, 3. Volcanic eruptions": 1,
        "What is the main cause of rising sea levels? 1. Melting glaciers, 2. Underwater earthquakes, 3. Increased rainfall": 1,
        "What greenhouse gas is most responsible for global warming? 1. Nitrogen, 2. Carbon dioxide, 3. Oxygen": 2,
        "What is a major consequence of climate change for coral reefs? 1. Increased growth, 2. Bleaching, 3. Better habitat conditions": 2,
        "Which energy source produces the least greenhouse gas emissions? 1. Coal, 2. Solar, 3. Natural gas": 2,
        "Which country emits the most carbon dioxide annually? 1. USA, 2. China, 3. India": 2,
        "What is the primary cause of climate change? 1. Deforestation, 2. Burning fossil fuels, 3. Increased volcanic activity": 2,
        "Which gas is released when permafrost thaws due to climate change? 1. Ozone, 2. Nitrous oxide, 3. Methane": 3,
        "What percentage of global greenhouse gas emissions come from the transportation sector? 1. 14%, 2. 25%, 3. 33%": 1,
        "Which of the following is NOT an effect of climate change? 1. More frequent heatwaves, 2. Ocean acidification, 3. Increased volcanic activity": 3,
        "What is the current concentration of carbon dioxide in the atmosphere (as of 2024)? 1. Around 390 ppm, 2. Around 414 ppm, 3. Around 450 ppm": 2
    }
    q = random.choice(list(questions.items()))
    print(q[1])
    await ctx.send(q[0])
    message = await ctx.send("Reply To This Message with 1️⃣ or 2️⃣ or 3️⃣")
    dood = message.id
    print(dood)
@bot.event
async def on_reaction_add(reaction, user):
    global dood
    global q
    if user.bot:
        return
    elif dood and reaction.message.id == dood:
        if reaction.emoji == "1️⃣":
            if q[1] == 1:
                await reaction.message.channel.send("You Are Correct!!!!1!!")
            else:
                await reaction.message.channel.send("you wrong so sad boo")
        if reaction.emoji == "2️⃣":
            if q[1] == 2:
                await reaction.message.channel.send("You Are Correct!!!!1!!")
            else:
                await reaction.message.channel.send("you wrong so sad boo")
        if reaction.emoji == "3️⃣":
            if q[1] == 3:
                await reaction.message.channel.send("You Are Correct!!!!1!!")
            else:
                await reaction.message.channel.send("you wrong so sad boo")

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
async def foodrate(ctx):
    await ctx.send("IS YOUR FOOD GOOD?")
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./safetodo/{file_name}")
            rate = (get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=f"safetodo/{file_name}"))
            print(rate)
            label = rate[0]
            confidence = rate[1]
            print(label)
            labelC = label.replace("\n", "")
            print(labelC)
            print(confidence)            
            if labelC == "Yummy food":
                await ctx.send("Its Good")
            elif labelC == "Disgusting Food":
                await ctx.send("Its NOT, it Sucks")

    else:    
        await ctx.send("No Food detected. send a food image with the command so that i can rate it")
@bot.command()
async def multiply(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

#show local file
@bot.command()
async def showfile(ctx, filename):
  """Sends a file as an attachment."""
  folder_path = "./nest/"
  file_path = os.path.join(folder_path, filename)
  try:
    await ctx.send(file=discord.File(file_path))
  except FileNotFoundError:
    await ctx.send(f"File '{filename}' not found.")

# upload file to local computer
@bot.command()
async def simpan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_url = attachment.url  IF URL
            await attachment.save(f"./nest/{file_name}")
            await ctx.send(f"Menyimpan {file_name}")
    else:
        await ctx.send("Anda lupa mengunggah :(")

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

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
      folder_path = "nest"  # Replace with the actual folder path
      files = os.listdir(folder_path)
      file_list = "\n".join(files)
      await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
      await ctx.send("Folder not found.")


#Computer Vision Deteksi objek
@bot.command()
async def deteksi(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(detect(input_image=f"./CV/{file_name}", output_image=f"./CV/{file_name}", model_path="yolov3.pt"))
            with open(f'CV/{file_name}', 'rb') as f:
                picture = discord.File(f)
            await ctx.send(file=picture)
    else:
        await ctx.send("Anda lupa mengunggah gambar :(")


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
async def sos(ctx, page: int = 0):
    await ctx.send('Welcome to the list of commands')
    await ctx.send("Use SOS and 0 to 2 for more commands")
    if page == 1:
        await ctx.send("-tulis (writes stuff to my computer or your computer or his computer) -tambahkan (im indonesian, also, this adds stuff to said computer file) -baca (reads file) -meme (gives you a random meme) -animeme (animal memes)- -pw (makes passwords) -sos (help, gives you info) -coinflip (flip a coin) -dice (dice)")
    elif page == 2:
        await ctx.send("-foodrate (rates your food trough AI) -rockpaperscissors (tock, peper, scissors)")
    elif page == 0:
        await ctx.send("-add (adds numbers) -subtract (subtracts numbers) -div (divides numbers) -multiply (multiplies numeros) -by (idk) -go (pokemon) -repeat (repeats a message) -dog (shows dog) -duck (duck) -climatrivia (gives you random trivia questions)")
    

@bot.command()
async def fightclub(ctx, fighter: str = "")


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

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here


bot.run('secret sausage, put your own secret sausage key here')
