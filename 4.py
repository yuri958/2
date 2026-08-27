meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            }

word = input("Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas): ")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("tem n")
    
