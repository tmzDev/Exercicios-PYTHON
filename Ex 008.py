# Ex 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Distancia em Metros : '))
print(f'A distancia de {m}m corresponde a ')
print(f'{m / 1000}Km \n{m / 100}hm \n{m / 10}dam')
print(f'{m * 10}dm \n{m *100}cm \n{m * 1000}mm')
