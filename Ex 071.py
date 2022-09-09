# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado 
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

n = int(input('Quantidade : '))
cinq = n // 50 
n %= 50 

vinte = n // 20
n %= 20 

dez = n // 10
n %= 10

um = n // 1

print(f'Você vai sacar \n{cinq} Notas de 50 \n{vinte} Notas de 20 \n{dez} Notas de 10 \n{um} Moedas de 1')

#### reescrever esse codigo 
