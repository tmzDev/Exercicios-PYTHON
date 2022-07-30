# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

p = [] 

for i in range(1,6):
    peso = float(input(f'Peso da {i}° pessoa : '))
    p.append(peso)

print(f'Menor peso digitado {min(p)} \nMaior peso digitado {max(p)}')
