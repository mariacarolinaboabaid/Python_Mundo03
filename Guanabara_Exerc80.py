#Quantidade de números que serão inseridos na Lista:
quantidade = input("Quantos números serão analisados? ")
while quantidade.isalpha() == True:
    print("Insira apenas dígitos numéricos.")
    quantidade = input("Quantos números serão analisados? ")
quantidade = int(quantidade)

#Pedindo os números para o Usuário:
numeros = []
for x in range(1, quantidade + 1):
    numero = input(f"Digite aqui o {x}º número: ")
    while numero.isalpha() == True:
        print("Insira apenas dígitos numéricos.")
        numero = input(f"Digite aqui o {x}º número: ")
    numero = int(numero)
    numeros.append(numero)

#Sorteando os números sem usar o método SORT().
numeros_sorteados = []
y = len(numeros) - 1
while y > - 1:
    if numeros[y] == min(numeros):
        numeros_sorteados.append(numeros[y])
        numeros.remove(numeros[y])
        y = y - 1

print(f"Os números digitados pelo Usuário em ordem crescente são: {numeros_sorteados}")