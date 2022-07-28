# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

n = int(input('Seu ano de nascimento : '))
idade = 2021 - n 

if idade < 9:
    print(f'Categoria : MIRIM ')
elif idade < 14:
    print('Categoria : INFANTIL')
elif idade < 19:
    print('Categoria : JÚNIOR')
elif idade < 25:
    print('Categoria : SÊNIOR')
else:
    print(f'Categoria : MASTER ')
