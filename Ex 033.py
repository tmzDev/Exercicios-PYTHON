#  Ex 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

l = []
for i in range(1,4):
    n = int(input(f'Digite o {i}° valor : '))
    l.append(n)

print(f'Menor {min(l)}   -   Maior {max(l)}')
