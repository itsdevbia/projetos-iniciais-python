import random

print ("Bem vindo ao jogo de Advinhação!")
print ("Tente advinhar o número que estou pensando entre 1 a 100")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = input("Digite seu palpite: ")

    if not palpite.isdigit():
        print ("Por favor, digite apenas números!")
        continue

    palpite = int(palpite)
    tentativas +=1

    if palpite < numero_secreto:
        print("É maior!!")
    elif palpite > numero_secreto:
        print ("É menor!!")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break

input("Pressione Enter para sair...")
      
