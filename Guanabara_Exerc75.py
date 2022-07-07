#Pedindo 4 números para o Usuário:
numero_1 = int(input("Número 1: "))
numero_2 = int(input("Número 2: "))
numero_3 = int(input("Número 3: "))
numero_4 = int(input("Número 4: "))

#Inserindo na Tupla:
tupla = (numero_1, numero_2, numero_3, numero_4)

#Verificando a ocorrência do nº 9:
if tupla.count(9) == 0:
    print("O número 9 não apareceu nenhuma vez.")
elif tupla.count(9) == 1:
    print("O número 9 apareceu uma única vez.")
else:
    print(f"O número 9 apareceu {tupla.count(9)} vezes.")

#Verificando a posição do nº 3:   

if tupla.count(3) != 0:
    print(f"A posição do 1º número 3 digitado é: {tupla.index(3) + 1}ª.")

#Verificando os nº pares e ímpares:
numeros_pares = []
numeros_impares = []
for numero in tupla:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

#Resultado números pares:
if len(numeros_pares) == 0:
    print(f"Nenhum número par foi dgitado.")
elif len(numeros_pares) == 1:
    print(f"O {numeros_pares} foi o único número par digitado.")
else:
    print(f"Os números pares digitados são: {numeros_pares}.")

#Resultado números ímpares:
if len(numeros_impares) == 0:
    print(f"Nenhum número ímpar foi dgitado.")
elif len(numeros_impares) == 1:
    print(f"O {numeros_impares} foi o único número ímpar digitado.")
else:
    print(f"Os números ímpares digitados são: {numeros_impares}.")