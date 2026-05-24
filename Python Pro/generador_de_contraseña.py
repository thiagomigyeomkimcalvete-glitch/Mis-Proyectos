import random

pregunta = int(input("Ingresa la cantidad de digitos que quieras"))
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""


for i in range(pregunta):
    caracter = random.choice(caracteres)
    password += caracter

print(password)