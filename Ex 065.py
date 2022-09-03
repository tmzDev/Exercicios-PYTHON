# Ex 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o 
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

lts = []
while True:
    n = int(input('Informe um numero inteiro : '))
    lts.append(n)

    op = input('Deseja continuar? [s / n] ').lower()
    if op == 'n':
        break 

print(f'Você digitou {len(lts)} numeros, a media foi {sum(lts) / len(lts)} \nO maior valor digitado foi {max(lts)} e o menor foi {min(lts)}')
