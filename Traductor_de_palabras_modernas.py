word = input("Escribe una palabra que no entiendas (con mayúsculas): ")
meme_dict = {
            "CRINGE": "Algo que te de verguenza ajena",
            "LOL": "Es cuando te quieres referir que algo es muy gracioso",
            "XD": "Es una cara riendose de lado"
            "CRUSH": "Es un término que se usa para referirte a la persona que te gusta"
            }

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Lo sinto, ni yo se que significa eso")


