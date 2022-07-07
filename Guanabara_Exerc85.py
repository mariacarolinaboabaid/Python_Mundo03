"""Vamos fazendo uma lista contendo listas de números pares e ímpares. 
Para completar as listas vamos pedir os números para o Usuário."""

#Importanto o módulo time:
from time import sleep

lista = [[], []]
#Pedindo os números para o Usuário:
for x in range(1, 8):
    numero = input(f"Número {x}: ")
    while numero.isalpha() == True:
        print("Digite apenas dígitos númericos. Tente novamente!")
        numero = input(f"Número {x}: ")
#Caso o número seja par:
    numero = int(numero)
    if numero % 2 == 0:
        lista[0].append(numero) 
#Caso o número seja ímpar:
    else:
        lista[1].append(numero)

#Sorteando a lista:
lista[0].sort()
lista[1].sort()
print("Arrumando os números em ordem crescente...")
sleep(1)
print("-'-" * 40)

#Resultado:
print(f"""Os números pares são: {lista[0]}.
Os números ímpares são: {lista[1]}.""")

