# Ex 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um 
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


s = float(input('Seu salario : R$'))
if s <= 1250:
    print(f'Seu salario de R${s:.2f} com reajuste de 15% é  ->  R${s / 100 *115:.2f}')
else:
    print(f'Seu salario de R${s:.2f} com reajuste de 10% é  ->  R${s / 100 * 110:.2f}')
    
