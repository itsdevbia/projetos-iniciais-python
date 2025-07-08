import random

print('🎮 Este é um jogo de adivinhação!')
print('Tente adivinhar o número secreto de acordo com a dificuldade escolhida.')

partidas = 0
acertos = 0

jogar_novamente = 's'

while jogar_novamente.lower() == 's':
    partidas += 1

    print("\nEscolha a dificuldade:")
    print("1 - Fácil (1 a 50)")
    print("2 - Médio (1 a 100)")
    print("3 - Difícil (1 a 200)")
    
    while True:
        dificuldade = input("Digite o número da dificuldade desejada: ")
        if dificuldade in ['1', '2', '3']:
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

    if dificuldade == '1':
        limite = 50
        max_tentativas = 10
    elif dificuldade == '2':
        limite = 100
        max_tentativas = 10
    else:
        limite = 200
        max_tentativas = 15

    numero_secreto = random.randint(1, limite)
    tentativas = 0
    palpites_feitos = []

    print(f"\n🔢 Adivinhe um número de 1 a {limite}. Você tem {max_tentativas} tentativas.")

    frases_erro = [
        "Hmm... ainda não!", 
        "Tente outra vez!", 
        "Quase lá!", 
        "Não foi dessa vez!", 
        "Você está chegando perto!"
    ]

    while tentativas < max_tentativas:
        palpite = input("Digite seu palpite: ")

        if not palpite.isdigit():
            print("❌ Por favor, digite apenas números!")
            continue

        palpite = int(palpite)
        palpites_feitos.append(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("📈 É maior!!", random.choice(frases_erro))
        elif palpite > numero_secreto:
            print("📉 É menor!!", random.choice(frases_erro))
        else:
            print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            acertos += 1
            break
        print(f"📋 Palpites até agora: {palpites_feitos}")

    else:
        print(f"\n😢 Você usou todas as {max_tentativas} tentativas.")
        print(f"O número secreto era: {numero_secreto}")

    print(f"\n🧮 Estatísticas: {partidas} partida(s), {acertos} acerto(s).")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")

print("\n🎊 Obrigada por jogar! Até a próxima!")
input("Aperte Enter para sair do jogo.")

