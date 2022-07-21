# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para 
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Largura da parede : '))
a = float(input('Altura da parede : '))
print(f'Dimensão {l} x {a}  =  {l * a}m²')
print(f'Tinta necessaria {(l * a) / 2:.1f}L de tinta')
