# Ex 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

n = int(input('Seu ano de nascimento : '))
ano = 2021 - n 

if ano < 18:
    print(f'Você ainda não pode se alistar, faltam {18 - ano} anos!')
elif ano > 18:
    print(f'Você esta atrasado {ano - 18} anos, procure imediatamente o posto do exercito!')
else:
    print(f'Você já pode se alistar, procure o posto mais proximo')
