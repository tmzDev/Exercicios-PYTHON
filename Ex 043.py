'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
p = float(input('Seu peso : '))
a = float(input('Sua altura : '))

imc = p / (a ** 2)
if imc < 18.5:
    print(f'IMC {imc:.2f}  -> ABAIXO DO PESO ')
elif imc < 25:
    print(f'IMC {imc:.2f}  -> PESO IDEAL')
elif imc < 30:
    print(f'IMC {imc:.2f}  -> SOBREPESO')
elif imc < 40:
    print(f'IMC {imc:.2f}  -> OBESIDADE')
else:
    print(f'IMC {imc:.2f}  -> OBESIDADE MORBIDA')
