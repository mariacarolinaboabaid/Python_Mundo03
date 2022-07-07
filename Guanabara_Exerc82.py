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

#Separando os números em pares ou ímpares:
numeros_pares = [] 
numeros_impares = []
for item in numeros:
    if item % 2 == 0:
        numeros_pares.append(item)
    else:
        numeros_impares.append(item)

print(f"""Os números pares são {numeros_pares}.
Os números ímpares são {numeros_impares}.""")