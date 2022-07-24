# Ex 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual foi o número 
# escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
a = random.randint(1, 10)

n = int(input('Chute um numero de 1 a 10 : '))
if n == a:
    print('Parabens você acertou!')
else:
    print(f'Você errou!, o numero era {a}')

