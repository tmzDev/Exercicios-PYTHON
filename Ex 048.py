# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

x = 0 
for i in range(3, 500, 6):
    if i % 3 == 0:
        x += i 
print(x)
