# Ex 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Valor do produto : R$'))
print(f'Valor  R${p:.2f} \nValor com desconto  R${p / 100 * 95:.2f}')
