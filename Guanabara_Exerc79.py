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
#Adicionando o número na Lista caso já não esteja:
    if numeros.count(numero) == 0:
        numeros.append(numero)

numeros.sort()
#Ordem crescente:
print(f"A ordem crescente dos números é: {numeros}.")