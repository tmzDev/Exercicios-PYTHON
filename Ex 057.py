# Ex 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter 
# um valor correto.

s = input('Informe seu sexo [m / f]: ').lower()
while True: 
  if s == 'm' or s == 'f':
    print(f'Sexo registrado')
    break
  else:
    s = input('Por favor insira uma opçaõ valida  : ').lower()
