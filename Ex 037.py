# Ex 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 
# 2 para octal e 3 para hexadecimal.

n = int(input('Digite um numero : '))
e = input('[1] - BINARIO \n[2] - OCTAL \n[3] - HEXADECIMAL \nSua escolha : ')
if e == '1':
    print(f'{bin(n)}')
elif e == '2':
    print(f'{oct(n)}')
elif e == '3':
    print(f'{hex(n)}')
