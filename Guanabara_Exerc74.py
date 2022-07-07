#OBJETIVO DO PROGRAMA: Perguntaremos ao Usuário quantos números aleatórios de '0' a '100' ele deseja sortear. Depois, mostraremos todos os números sorteados, o maior e o menor números.

#Importando os módulos:
from random import randint
from time import sleep

#Quantidade de número a ser sorteada:
quantidade = input("Quantos números devem ser sorteados? ")
while quantidade.isalpha() == True:
    print("Insira apenas dígitos númericos. ")
    sleep(1)
    quantidade = input("Quantos números devem ser sorteados?")

quantidade = int(quantidade)

#Sorteado os números:
numeros_aleatorios = []
for x in range(quantidade):
    x = randint(0, 100)
    numeros_aleatorios.append(x)

numeros_aleatorios = tuple(numeros_aleatorios)

#Resultado:
print(f'''Os números sorteados são {numeros_aleatorios}.
O menor número é: {min(numeros_aleatorios)}
O maior número é: {max(numeros_aleatorios)}''')
