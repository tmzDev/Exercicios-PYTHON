'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

n = float(input('Valor do produto : '))
pg = input('Forma de pagamento \n[1] - À Vista \n[2] - À vista cartão \n[3] - Até 2x Cartão \n[4] - 3x ou mais \nopção desejada : ')

if pg == '1':
    print(f'O valor de R${n:.2f} com desconto de 10%   =   R${n / 100 * 90:.2f}')
elif pg == '2':
    print(f'O valor de R${n:.2f} com desconto de 5%     =  R${n / 100 * 95:.2f}')
elif pg == '3':
    print(f'O valor de R${n:.2f} parcelado em 2x de  =   R${n / 2 :.2f}')
elif pg == '4': 
    p = int(input('Quantidade de parcelas : '))
    print(f'O valor de R${n:.2f} com acrescimo de 20% dividido em {p}x   =  R${(n / 100 * 120) / p :.2f}')
