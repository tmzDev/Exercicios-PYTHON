# Ex 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Velocidade : '))
if v > 80:
    print('Voce esta acima do limite de 80 Km/h')
    print(f'Valor da multa : R${(v - 80) * 7:.2f}')
else:
    print('Você esta no limite, dirija com segurança')
