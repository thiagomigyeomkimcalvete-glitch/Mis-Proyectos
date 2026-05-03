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

bot.run("PON TU PASSWORD AQUI")
