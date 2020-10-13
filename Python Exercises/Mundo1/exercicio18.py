# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulos

import math

angulo = int(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem seno de {sen:.2f}, cosseno de {cos:.2f} e tangente de {tg:.2f}.')
