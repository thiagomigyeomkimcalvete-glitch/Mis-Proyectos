import random

dado = random.randint(1,20)
count = 1

while True:
    intentos = int(input("Intento " + str(count) + ": Adivina el numero del 1 al 20:"))

    if intentos == dado:
        print("No quedan más intentos. El número secreto era",intentos)
        break
    elif intentos < dado:
        print("El número secreto es mayor")
    else:  
        print("El número secreto es menor")

    count += 1
