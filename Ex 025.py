# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = input('Seu nome : ').lower()
print(f'Tem silva no nome ? {"Sim" if "silva" in n else "Não"}')
