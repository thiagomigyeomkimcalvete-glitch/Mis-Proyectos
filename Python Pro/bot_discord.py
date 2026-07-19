import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def chiste(ctx):
    await ctx.send('- Oye, vos sabés cómo se escribe nariz en ingles?                                                                               -Nose                                                                                                                                                              -Es para un examen                                                                                                                                    -Nose                                                                                                                                                              -¿Por qué nadie lo sabe?')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Si, este bot es cool.')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def password(ctx, longitud:int):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(longitud):
        password += random.choice(elements)

    await ctx.send("tu clave es:" + password)

@bot.command()
async def tips(ctx):
    numero = random.randint(1, 9)
    text_path = f"Consejos_Ecologicos/Consejo{numero}.txt"

    if not os.path.exists(text_path):
        await ctx.send("No se encontró el archivo de consejo.")
        return
    
    with open(text_path, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    await ctx.send(contenido)
@bot.command()
async def mem(ctx):
    num = random.randint(1, 5)
    images = os.listdir("images")
    image = random.choice(images)

    if num in (1, 2):
        image_path = "images/Meme1.jpeg"
    elif num in (3, 4):
        image_path = "images/Chat_GPT_VS_Claude.jpg"
    else:
        images = os.listdir("images")
        image_path = f"images/{random.choice(images)}"
    if not os.path.exists(image_path):
        await ctx.send("No se encontró la imagen.")
        return

    with open(image_path, "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

    # Escribir en el archivo de texto
    with open("text.txt", "a", encoding="utf-8") as f:
        f.write("XD\n")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command(name = 'duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")