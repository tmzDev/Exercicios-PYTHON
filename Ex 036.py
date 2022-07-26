# Ex 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos 
# nos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

cs = float(input('Valor da casa : '))
sl = float(input('Seu salario : '))
an = int(input('Quantos ano pretende pagar? : '))

ms = an * 12
pr = cs / ms
if pr > sl / 100 * 30:
    print(f'O valor da prestação é R${pr:.2f} \nEmprestimo negado')
else:
    print(f'O valor da prestação é R${pr:.2f} \nEmprestimo Aprovado')
