# Ex 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

m = 0
for i in range(1,8):
    n = int(input(f'Digite a idade da {i}° pessoa : '))
    if n >= 18:
        m += 1
print(f'Das 7 idades apresentadas, {m} são maiores de idade')
