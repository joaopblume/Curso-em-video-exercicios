# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

r1 = int(input('Valor do primeiro segmento: '))
r2 = int(input('Valor do segundo segmento: '))
r3 = int(input('Valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
