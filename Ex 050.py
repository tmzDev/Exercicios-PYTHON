# Ex 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

lts = []
for i in range(1, 7):
    n = int(input(f'Informe o {i}° numero : '))
    if n % 2 == 0:
        lts.append(n)
print(f'A soma de todos os pares foi {sum(lts)}')
