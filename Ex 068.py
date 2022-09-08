# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de 
# vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint as rand
v = 0 

print(f'JOGO DO PAR OU IMPAR \n')
while True:
    num = rand(1, 10)

    n = int(input('Escolha um numero : '))
    op = input('PAR ou IMPAR [P / I] :  ').lower()
   
    total = n + num

    if total % 2 == 0  and op == 'p':
        print(f'\nVocê escolheu {n} e o computador {num}    {n + num} = PAR')
        print(f'Parabens você ganhou! \n')
        v += 1
    
    elif total % 2 == 1 and op == 'i':
        print(f'\nVocê escolheu {n} e o computador {num}    {n + num} = IMPAR')
        print(f'Parabens você ganhou! \n')
        v += 1
    
    elif total % 2 == 1 and op == 'p':
        print(f'\nVocê escolheu {n} e o computador {num}    {n + num} = IMPAR')
        break
    elif total % 2 == 0 and op == 'i':
        print(f'\nVocê escolheu {n} e o computador {num}    {n + num} = PAR')
        break

print(f'GAME OVER! Você ganhou {v} partidas \n')
