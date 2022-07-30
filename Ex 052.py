# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

x = 0
num = []
n = int(input('Digite um numero : '))
for i in range(n, 0, -1):
    if n % i == 0:
        num.append(i)
        x += 1
if x == 2:
    print(f'{n} é PRIMO')
else:
    print(f'{n} NÃO É PRIMO, pois foi dividido pelos numeros -> ', end =" ")
    print(*num)
