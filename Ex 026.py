# Ex 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira 
# vez e em que posição ela aparece a última vez

f = input('Digite uma frase : ').lower().strip()

print(f'A aparece {f.count("a")} vezes')
print(f'Primeira posição de A {f.find("a") + 1}')
print(f'Ultima posição de A {f.rfind("a") + 1}')
