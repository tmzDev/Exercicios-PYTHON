# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

min = maior = total = 0
nome_min = '' 

nome = input('Nome do produto : ')
preco = int(input('Preco do produto : '))
min = preco 
nome_min = nome 
total += preco
if preco > 1000:
    maior += 1

while True:
    nome = input('Nome do produto : ')
    preco = int(input('Preço do produto : '))
    if preco < min:
        min = preco 
        nome_min = nome 
    if preco > 1000:
        maior += 1 
    total += preco 

    op = input('Deseja continuar? [S / N] : ')
    if op == 'n':
        break 

print(f'\nO total foi R${total:.2f} \nTemos {maior} produtos custando mais de R$ 1000.00 \nO produto mais barato foi {nome_min} R$ {min:.2f}')




    
