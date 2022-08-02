# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n1 = int(input('Digite um número inteiro qualquer: '))
a = 1
for n1 in range(n1, 0, -1):
    a *= n1
print(f'{a}')
