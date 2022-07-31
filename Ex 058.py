# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar 
# até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random 
num = random.randint(1, 20)

t = 0

n = int(input('Chute um numero entre 1 e 20 : ' ))
while True:
    if n == num:
        t += 1
        break 
    elif n > num:
        n = int(input('Chute um numero mais baixo : '))
        t += 1
    elif n < num:
        n = int(input('Chute um numero mais alto : '))
        t += 1
    
print(f'O jogo acabou, Total de tentativas {t}')
