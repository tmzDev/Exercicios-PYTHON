# Ex 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

n = input('Nome da cidade : ').lower().strip().split()
print('Verdadeiro' if n[0] == 'santo' else 'Falso')
