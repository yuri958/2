import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("Digite o comprimento da senha: "))
senha_gerada = ""
for i in range(comprimento):
    caractere_aleatorio = random.choice(caracteres)
    senha_gerada += caractere_aleatorio

print("Senha gerada:", senha_gerada)
