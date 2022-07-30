# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('primeiro termo : '))
r = int(input('Razão : '))
for i in range(pt, pt + 10 * r, r):
    print(i, end = ' ')
