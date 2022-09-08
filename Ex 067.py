# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será 
# interrompido quando o número solicitado for negativo. 

while True:
    n = int(input('Qual numero para tabuada : '))
    if n < 0:
        print('Programa encerrado')
        break
    else:
        for i in range(1, 11):
            print(f'{n} x {i} = {i * n}')
    print('_' * 50)
