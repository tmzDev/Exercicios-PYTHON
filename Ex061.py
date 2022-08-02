# Ex 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


pt = int(input('Primeiro termo : '))
rz = int(input('Razão : '))
x = v = 0
while x < 10:
    print(f'{pt} ->', end=' ')
    pt += rz 
    x += 1
print('FIM')
