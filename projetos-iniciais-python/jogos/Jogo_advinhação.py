import random

print('Este é um jogo de adivinhação!')
print('Tente adivinhar um número de 1 a 100')

jogar_novamente = 's'

while jogar_novamente.lower() == 's':
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = input("Digite seu palpite: ")

        if not palpite.isdigit():
            print("Por favor, digite apenas números!")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("É maior!!")
        elif palpite > numero_secreto:
            print("É menor!!")
        else:
            print(f"Parabéns! Você descobriu o número {numero_secreto} em {tentativas} tentativas!")
            break

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")

    if jogar_novamente.lower() == 's':
        print ("Vamos jogar de novo!!")
    else:
        print ("Obrigada por jogar!!")
        input("Aperte Enter para sair do jogo.")
      
