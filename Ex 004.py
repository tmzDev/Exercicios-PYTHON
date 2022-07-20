# Ex 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

v = input('Qualquer coisa: ')
print(f'{v} é um alphanum? : {v.isalnum()}')
print(f'{v} é um decimal? : {v.isdecimal()}')
print(f'{v} é um digito? : {v.isdigit()}')
print(f'{v} esta em minusculo? : {v.islower()}')
print(f'{v} está em maiusculo? : {v.isupper()}')
print(f'{v} é um numerico? : {v.isnumeric()}')
print(f'{v} é um ascii : {v.isascii()}')
