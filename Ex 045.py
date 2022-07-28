# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random 

lts = ['pedra', 'papel', 'tesoura']
pc = random.choice(lts)

esc = input('[1] - PEDRA \n[2] - PAPEL \n[3] - TESOURA \nSua escolha : ')
if esc == '1' and pc == 'pedra':
    print('EMPATE - Ambos escolheram pedra')
elif esc == '1' and pc == 'papel':
    print(f'DERROTA - O pc escolheu papel')
elif esc == '1' and pc == 'tesoura':
    print(f'GANHOU - O pc escolheu tesoura')
elif esc == '2' and pc == 'pedra':
    print(f'GANHOU - O pc escolheu pedra')
elif esc == '2' and pc == 'papel':
    print(f'EMPATE - AMbos escolheram papel')
elif esc == '2' and pc == 'tesoura':
    print(f'DERROTA - O pc escolheu tesoura')
elif esc == '3' and pc == 'pedra':
    print(f'DERROTA - O pc escolheu pedra')
elif esc == '3' and pc == 'papel':
    print(f'GANHOU - O pc escolheu papel')
elif esc == '3' and pc == 'tesoura':
    print(f'EMPATE - Ambos escolheram tesoura')
