# Ex 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro numero : '))
n2 = int(input('Segundo numero : '))

if n1 == n2:
    print(f'Os dois valores são iguais :D')
elif n1 > n2:
    print(f'O primeiro numero é maior')
else:
    print(f'O segundo numero é maior')
