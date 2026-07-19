import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$Dame un chiste'):
        await message.channel.send("- Oye, vos sabés cómo se escribe nariz en ingles?                                                                               -Nose                                                                                                                                                              -Es para un examen                                                                                                                                    -Nose                                                                                                                                                              -¿Por qué nadie lo sabe?")
    
    elif message.content.startswith('$Clave'):
        import random

        elements = "+-/*!&$#?=@<>"
        password = ""
        pass_length = int(input("Enter pass length: "))

        for i in range(pass_length):
            password += random.choice(elements)

        print(password)
    else:
        await message.channel.send(message.content)

client.run("MTQ5NTU0MDE3NTQ2NjM5NzY5Nw.GrFfNZ.t4rEXRIOqFi2qGWeJdVtdnLn7KVCzvSr5VwWGk")