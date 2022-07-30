# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

n = input('Digite uma frase ou palavra : ').strip()
x = n.replace(' ','')
if x == x[::-1]:
    print(f'{n} é um PALINDROMO')
else:
    print(f'{n} não é um PALINDROMO')
