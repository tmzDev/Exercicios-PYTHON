# Ex 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando 
# ele disser que quer mostrar 0 termos.

pt = int(input('Primeiro termo : '))
rz = int(input('Razão : '))
n = 0
while n <10:
    print(f'{pt} -> ', end =' ')
    pt += rz
    n += 1
print()
o = 1
while o != 0:
    o = int(input('Mais quantos termos quer mostrar? '))
    for i in range(o + 1, 1, -1):
        print(f'{pt} ->', end= ' ')
        pt += rz
        n += 1 
    print()
print(f'No total foram mostrados {n} termos')
