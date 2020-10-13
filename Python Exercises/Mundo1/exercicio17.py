# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Cateto opostos: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)

print(f'A hipotenusa será igual a {hip:.2f}.')
