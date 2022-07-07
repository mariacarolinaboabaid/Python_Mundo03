#Objetivo do programa = Listagem de produtos e preços printada em forma tabular.

listagem = ("Lápis", '1.75',
"Borracha", '2.00',
"Apontador", '4.80',
"Mochila", '55.50',
"Lancheira", '40.00',
"Caneta", '2.50',
"Tesoura", '6.25')

print('-'* 39)
print("LISTAGEM DE PREÇOS")
print('-'* 39)
for produto in range(0, len(listagem), 2):
    item = listagem[produto].ljust(30, '.')
    preço = listagem[produto +1].rjust(5)
    print(f'{item}R$ {preço}')
print('-'* 39)