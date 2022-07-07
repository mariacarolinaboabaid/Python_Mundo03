"""Vamos montar uma matriz conforme dimensão dada pelo Usuário e com os valores também dados pelo o Usuário.
Para cada linha da matriz, informaremos os números pares e a sua soma, os números ímpares e a sua soma, a soma total da linha, e o menor e maior número de cada linha."""

#Dimensões da matriz:
matriz = []

quantidade_listas = input("Qual a altura da matriz? ")
while quantidade_listas.isalpha() == True:
    print("Digite apenas dígitos númericos. Tente novamente!")
    quantidade_listas = input("Qual a altura da matriz? ")
quantidade_listas = int(quantidade_listas)

tamanho_lista = input("Qual a largura da matriz? ")
while tamanho_lista.isalpha() == True:
    print("Digite apenas dígitos númericos. Tente novamente!")
    tamanho_lista = input("Qual a largura da matriz? ")
tamanho_lista =  int(tamanho_lista)

#Construindo a matriz:
for x in range(quantidade_listas):
    matriz.append([])
    for y in range(tamanho_lista):
        numero = input(f"Digite o número para [{x}][{y}]: ")
        while numero.isalpha() == True:
            print("Apenas dígitos numéricos são válidos. Tente novamente!")
            numero0 = input(f"Digite o número para [0][{x}]: ")
        matriz[x].append(numero)

#Imprimindo a matriz:
print("=-=" * 40)
print()
for z in range(quantidade_listas):
    for w in range(tamanho_lista):
        print(f"[{matriz[z][w].rjust(5)}]", end=" ")
    print()

#Efeito visual:
print()
print("=-=" * 40)
print()

#Separando os números da linha em par e em ímpar:
pares = []
impares = []
for a in range(quantidade_listas):
    pares.append([])
    impares.append([])
    for b in range(tamanho_lista):
        matriz[a][b] = int(matriz[a][b])
        if matriz[a][b] % 2 == 0:
            pares[a].append(matriz[a][b])
        else:
            impares[a].append(matriz[a][b])
#Números pares:
    if len(pares[a]) == 1:
        print(f"O valor par da linha {a + 1}ª é: {pares[a]}.")
    elif len(pares[a]) > 1:
        print(f"Os valores pares da linha {a + 1}ª são {pares[a]}, e a sua soma é de {sum(pares[a])}.")
    else:
        print(f"Não há nenhum valor par na linha {a + 1}ª.")
#Números ímpares:
    if len(impares[a]) ==1:
        print(f"O valor ímpar da linha {a + 1}ª é: {impares[a]}.")
    elif len(impares[a]) > 1:
        print(f"Os valores ímpares da linha {a + 1}ª são {impares[a]}, e a sua soma é de {sum(impares[a])}.")
    else: 
        print(f"Não há nenhum valor ímpar na linha {a + 1}ª.")
#Mosttrando o menor e maior número e a soma dos números da linha:
    print(f"""A soma dos valores da linha {a + 1}ª é {sum(matriz[a])}.
O menor número da linha {a + 1}ª é {min(matriz[a])}.
O maior número da linha {a + 1}ª é {max(matriz[a])}.""")
    print()
    


