# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

idade = homem = mulher_idade = 0
while True:
    i = int(input('Idade do usuario : '))
    s = input('Sexo do usuario  [M / F] : ')
   
    print()

    if i >= 18:
        idade += 1
    if s == 'm':
        homem += 1
    if s == 'f' and i < 20:
        mulher_idade += 1


    op = input('Deseja continuar? [S / N] : ')
    if op == 'n':
        break

print(f'{homem} Homens Foram cadastrados!')
print(f'{idade} pessoas cadastradas são maiores de idade!')
print(f'{mulher_idade} Mulheres com menos de 20 anos Foram cadastrados!\n')
    
