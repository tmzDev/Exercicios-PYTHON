# Ex 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input('Seu nome : ').split()

print(f'Primeiro -> {n[0]}')
print(f'Ultimo -> {n[-1]}') 
# Ou  print(f'Ultimo -> {n[len(n) -1]}')
