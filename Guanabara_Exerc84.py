#Objetivo do programa = Vamos pedir os pesos de varias pessoas e listar as mais pesadas e as mais leves

#Importando módulos:
from time import sleep

#Perguntando ao Usuário a quantidade de pessoas:
quantidade = input("De quantas pessoas vamos ler os seus nomes e pesos? ")
while quantidade.isalpha() == True:
    print("Apenas dígitos numéricos são válidos. Tente novamente!")
    quantidade = input("De quantas pessoas vamos ler os pesos? ")
quantidade = int(quantidade)

peso_nome = [] 
ranking = []
#Lendo os nomes e os pesos:
for x in range(1, quantidade + 1):
    nome = input(f"Insira o nome da pessoa {x}: ")
    peso = input(f"Insira o peso da pessoa {x}: ")
    while peso.isalpha() == True:
        print("Apenas dígitos numéricos são válidos. Tente novamente!")
        peso = input(f"Insira o peso da pessoa {x}: ")
    peso = float(peso)
    peso_nome.append(peso)
    peso_nome.append(nome)
    ranking.append(peso_nome[:])
    peso_nome.clear()

#Efeitos:
print("Calculando o resultado...")
sleep(1)
print("--" * 40)

#Sorteando a lista em ordem crescente:
ranking.sort()

#Resultado do(s) menor(es) pesos:
print(f"Ao todo você cadastrou {quantidade} pessoas.\n")
if ranking [0][0] != ranking [1][0]:
    print(f"O menor peso é {ranking[0][0]:.2f}kg, sendo o peso do(a) {ranking[0][1]}.")
#elif ranking [0][0] == ranking [1][0]:
    #print(f"O menor peso é {ranking[0][0]} dos(as) {ranking[0][1]} e {ranking[1][1]}.")
else:
    print(f"O menor peso é {ranking[0][0]:.2f}kg, sendo o peso do(a): {ranking[0][1]}", end= " ")
    for y in range(1, quantidade):
        if  ranking[0][0] == ranking [y][0]: 
            print(f"{ranking[y][1]}", end= " ")
print("\n")

#Sorteando a lista em ordem decrescente:
ranking.sort(reverse=True)

#Resultado do(s) maior(es) pesos
if ranking [0][0] != ranking [1][0]:
    print(f"O maior peso é {ranking[0][0]:.2f}kg, sendo o peso do(a): {ranking[0][1]}.")
#elif ranking [0][0] == ranking [1][0]:
    #print(f"O menor peso é {ranking[0][0]} dos(as) {ranking[0][1]} e {ranking[1][1]}.")
else:
    print(f"O maior peso é {ranking[0][0]:.2f}kg, sendo o peso do(a): {ranking[0][1]}", end= " ")
    for y in range(1, quantidade):
        if  ranking[0][0] == ranking [y][0]: 
            print(f"{ranking[y][1]}", end= " ")
