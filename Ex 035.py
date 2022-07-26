# Ex 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Informe o 1º segmento: '))
b = int(input('Informe o 2º segmento: '))
c = int(input('Informe o 3º segmento: '))

print('Os segmentos acima PODEM FORMAR um triângulo.' if a + b > c and b + c > a and a + c > b else 'Os segmentos acima NÃO PODEM formar um triângulo')
