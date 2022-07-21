# Ex 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Salario : '))
print(f'R${s:.2f} \nR${s / 100 * 115:.2f} Com reajuste')
