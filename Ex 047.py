# Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

x = 0
for i in range(1, 51):
    if i % 2 == 0:
        print(f'{i} ->', end=" ")
print('FIM ')
