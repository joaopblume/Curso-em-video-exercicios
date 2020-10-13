# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de material de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura} x {altura}, totalizando uma área de {area}m².')
print(f'Para pintar sua parede você precisará de {tinta}l de tinta!')