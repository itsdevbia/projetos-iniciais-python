
print ("Ola! Coloque suas informações abaixo:")

from datetime import datetime 

while True:
    nome = input ("Nome completo: ")
    if nome.replace (" ", "").isalpha():
        break
    else:
        print("Por favor, digite um nome valido (apenas letras).")

while True:
    CPF = input("CPF: ")
    if CPF.isdigit() and len(CPF) == 11:
        CPF_formato = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"
        break
    else:
        print (" CPF invalido! Digite apenas os 11 números.")

while True:
    data_nascimento = input("Data de nascimento: ")
    try:
        data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y")
        break
    except ValueError:
        print("formato inválido! use o formato dd/mm/aaaa e insira uma data real.")
  
print (f"Olá, {nome}! Você nasceu em {data_nascimento} e possui o CPF {CPF_formato}.")
print ("Obrigada por compartilhar suas informções!")

input("Pressione Enter para sair...")