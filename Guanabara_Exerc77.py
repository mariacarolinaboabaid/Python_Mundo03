#Para cada palavra da Tupla, iremos mostrar suas vogais.

#Criando a Tupla:
tupla = ('Alexandre', 'Henrique', 'Fernandes', 'Nolla', 'Maria', 'Carolina', 'Knudsen', 'Boabaid')

#Verificando as vogais:
for name in range(len(tupla)):
    print(f'A palavra {tupla[name]} tem as seguintes vogais: ', end= "")
    for letter in range(len(tupla[name])):
        if tupla[name][letter] in 'A E I O U a e i o u':
            print(f'{tupla[name][letter]}', end= " ")
    print("\n")