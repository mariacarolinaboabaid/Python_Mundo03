#Quantidade de números que serão inseridos na Lista:
quantidade = input("Quantos números serão analisados? ")
while quantidade.isalpha() == True:
    print("Insira apenas dígitos numéricos.")
    quantidade = input("Quantos números serão analisados? ")
quantidade = int(quantidade)

#Adicionando os números na Lista:
numeros = []
for x in range(1, quantidade + 1):
    numero = input(f"Digite aqui o {x}º número: ")
    while numero.isalpha() == True:
        print("Insira apenas dígitos numéricos.")
        numero = input(f"Digite aqui o {x}º número: ")
    numero = int(numero)
    numeros.append(numero)

#Mostrando o maior e o menor número:
print(f"Os números inseridos foram: {numeros}.")
print(f"O menor número inserido é {min(numeros)} e está na posição {numeros.index(min(numeros)) + 1}ª.")
print(f"O maior número inserido é {max(numeros)} e está na posição {numeros.index(max(numeros)) + 1}ª.")