# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# formula ((9 * C) / 5) + 32

c = float(input('Temperatura em °C : '))
print(f'°C convertido {((9 * c) / 5 ) + 32:.1f}°F')
