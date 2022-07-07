#-*- coding: utf-8 -*-
#Objetivo do programa: Verificar se a expressão dada pelo Usuário contendo parênteses está correta.

#Pedindo a expressão para o Usuário:
frase = input("Digite aqui uma  expressão usando parênteses: ")
while "(" and ")" not in frase:
    print("A frase deve conter parênteses.")
    frase = input("Digite aqui uma frase usando parênteses: ")

#Verificando se o número de '(' é igual ao número de ')':
if frase.count("(") > frase.count(")"):
    print("A contagem dos parênteses está incorreta. Há mais '(' do que ')'.")
    quit
elif frase.count("(")< frase.count(")"):
    print("A contagem dos parênteses está incorreta. Há mais ')' do que '('.")
    quit
#Se o número de '(' for igual ao número de ')': 
else:
    abertura_parenteses = []
    fechamento_parenteses = []
    for carater in range(len(frase)):
        if frase[carater] == "(":
            index = frase.index(frase[carater], carater)
            abertura_parenteses.append(index)
        elif frase[carater] == ")":
            index = frase.index(frase[carater], carater)
            fechamento_parenteses.append(index)
#Verificando se ordem de fechamento dos parênteses está correta:
    for posicao in range(len(abertura_parenteses)):
#Quando a posição dos parênteses não estiver correta:
        if abertura_parenteses[posicao] > fechamento_parenteses[posicao]:
            print("A sua expressão está incorreta.")
            break
#Quando a posição dos parênteses estiver correta:
        elif posicao == len(abertura_parenteses) - 1:
            print("A sua expressão está correta.")

    
