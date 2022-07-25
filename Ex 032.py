# Ex 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

n = int(input('Digite o ano : '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'{n} - BISSEXTO')
else:
    print(f'{n} - NÃO É BISSEXTO')
