#Perguntando qual será o tamanho da Lista:
tamanho = input("Quantos números serão adicionados na lista? ")
while tamanho.isalpha() == True:
    print("Insira apenas digítos numéricos!")
    tamanho = input("Quantos números serão adicionados na lista? ")
tamanho = int(tamanho)

#Pedindo os números para o Usuário e adicionando à Lista:
numeros = []
for x in range(1, tamanho + 1):
    numero = input(f"Digite o {x}º: ")
    while numero.isalpha() == True:
        print("Insira apenas digítos numéricos!")
        numero = input(f"Digite o {x}º: ")
    numero = int(numero)
    numeros.append(numero)

#Mostrando a ordem crescente e decrescente dos números inseridos pelo Usuário:
numeros.sort()
print(f"A ordem crescente dos números digitados é: {numeros}.")
numeros.sort(reverse=True)
print(f"A ordem decrescente dos números digitados é: {numeros}.")

#Perguntando ao Usuário se quer procurar um número na Lista:
option = 'S'
while option == 'S':
    option = input("Deseja procurar algum número específico na lista? [S \ N] ").strip().upper()[0]
    while option not in "S N":
        print("A resposta deve ser apenas 'Sim' ou 'Não'.")
        option = input("Deseja procurar algum número específico na lista? [S \ N] ").strip().upper()[0]
    if option == "S": 
        numero_procurado = input("Que número você deseja procurar? ")
        if numeros.count(numero_procurado) == 1:
            print(f"O numéro {numero_procurado} está na lista, na posição {(numeros.index(numero_procurado) + 1)}.")
        else:
            print(f"O número {numero_procurado} não está na lista.")
    if option == "N":
        break

