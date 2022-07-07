#OBJETIVO DO PROGRAMA: Criar uma tupla com os 20 primeiros colocados do Brasileirão, mostrando os 5 primeiros colocados, os quatros últimos colocados e os times em ordem alfabética.

times = ('Palmeiras', 'Atlético', 'Corinthians', 'Coritiba', 'São Paulo', 'Athletico-PR', 'Botafogo', 'Flamengo', 'Santos', 'América-MG', 'Fluminense', 'Avaí', 'Bragantino', 'Internacional', 'Goiás', 'Cuiabá', 'Juventude', 'Ceará - SC', 'Atlético - GO', 'Fortaleza')

#MOSTRANDO OS PRIMEIROS 5 COLOCADOS:
print("\033[1mOS CINCO PRIMEIROS COLOCADOS:\033[m")
x = 1
for time in range(0, 5):
    print(f'O {x}º colocado é {times[time]}.')
    x = x + 1
print('\n')

#MOSTRANDO OS QUATRO ÚLTIMOS COLOCADOS:
print("\033[1mOS QUATRO ÚLTIMOS COLOCADOS:\033[m")
a = 20
for time in range (0, 5):
    print(f'O {a}º colocado é {times[a - 1]}.')
    a = a - 1
print('\n')

#MOSTRANDO OS TIMES EM ORDEM ALFABÉTICA:
print(f"\033[1mOS TIMES EM ORDEM ALFABÉTICA SÃO: {sorted(times)}.\033[m")


