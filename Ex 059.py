"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Informe o primeiro valor : '))
n2 = int(input('Informe o segundo valor : '))
while True:
    op = input('[1] - SOMAR \n[2] - MULTIPLICAR \n[3] - MAIOR \n[4] - NOVOS NUMEROS \n[5] - SAIR \nInforme sua escolha : ')
    if op == '1':
        print(f'{n1} + {n2} = {n1 + n2}\n')
    elif op == '2':
        print(f'{n1} x {n2} = {n1 * n2}\n')
    elif op == '3':
        if n1 > n2:
            print(f'O primeiro numero digitado é maior\n')
        elif n1 < n2:
            print(f'O segundo numerdo digitado é maior\n')
        else:
            print(f'Os dois valores são iguais\n')
    elif op == '4':
        n1 = int(input('Informe o novo valor : '))
        n2 = int(input('Informe o segundo novo valor : '))
    elif op == '5':
        print('Obrigado por utilizar nosso app')
        break 
    else:
        print(f'Por favor digite uma opção valida\n')
