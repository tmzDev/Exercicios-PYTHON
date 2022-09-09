# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler
#  um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um numero de 0 a 20 : '))
    if n >= 0 and n <= 20:
        print(f'Você digitou o numero : {num[n]}')
        break 
    else:
        print('Por favor digite um numero valido!')
