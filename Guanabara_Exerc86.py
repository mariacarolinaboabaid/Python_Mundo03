#Vamos montar uma matriz conforme dimensão dada pelo Usuário e com os valores também dados pelo o Usuário.

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
for z in range(quantidade_listas):
    for w in range(tamanho_lista):
        print(f"[{matriz[z][w].rjust(5)}]", end=" ")
    print()

