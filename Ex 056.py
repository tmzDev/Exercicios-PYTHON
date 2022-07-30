"""
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o
nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""


ih = im = me =  0
n = ''
for i in range(1,5):
    nome = input('Nome : ')
    sexo = input('Sexo : ')
    idade = int(input('Idade : '))

    me += idade

    if sexo == 'm' and idade > ih:
        n = nome 
        ih = idade

    if sexo == 'f' and idade >= 20:
        im += 1
print(f'Media de idade : {me / 4}')
print(f'O {n} é o homem mais velho, {ih} anos ')
print(f'{im} mulheres tem mais de 20 anos ')
