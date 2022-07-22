# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

n = input('Seu nome completo : ')
print(f'Nome minusculo : {n.lower()}')
print(f'Nome maiusculo : {n.upper()}')
t = n.replace(' ','')
print(f'Quantidade de letras : {len(t)}')
x = n.split()
print(f'Letras primeiro nome : {len(x[0])}')

