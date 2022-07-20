# Ex 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

r = float(input('Quantos reais na carteira? R$'))

print(f'Com R$ {r:.2f} você pode comprar USD {r / 5.46:.2f}')
# Dolar no dia 20/07/22  -> 5.46
