# Ex 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias alugados? : '))
km = int(input('Quantos Km rodados? : '))

print(f'\nO total a pagar é R${km * 0.15 + d * 60:.2f}') 
