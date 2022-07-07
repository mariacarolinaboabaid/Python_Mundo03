#OBJETIVO DO PROGRAMA: Criar uma tupla contendo os números de "0" a "20", e mostrar o número escolhido pelo Usuário.

#CRIANDO A TUPLA:
numbers = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

escolha = 'S'
#PEDINDO O NÚMERO PARA O USUÁRIO:
while escolha == 'S':
    choosen_number = input("Escolha um número entre '0' a '20': ")
    while choosen_number.isalpha() == True or int(choosen_number) > 20 or int(choosen_number) < 0:
        choosen_number = input("\033[31mInsira apenas dígitos numéricos entre '0' a '20'.\033[m Escolha novamente um número entre '0' a '20': ")
    choosen_number = int(choosen_number)
#PRINTANDO O RESULTADO:
    print(f'O número escolhido é {numbers[choosen_number]}.')
#PERGUNTANDO SE O USUÁRIO DESEJA ESCOLHER OUTRO NÚMERO:
    escolha = input("Deseja escolher outro número? [Sim / Não]: ").strip().upper()[0]
    while escolha not in "S N":
        escolha = input("\033[31mInserir apenas 'sim' ou 'não'. \033[34m Deseja continuar? [S/N] \033[m").strip().upper()[0]

#FIM
print("Fim!")