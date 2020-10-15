# Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
# será formado.
"""
> Equiláterio: todos os lados iguais
> Isóceles: dois lados iguais
> Escaleno: todos os lados diferentes
"""

r1 = int(input('Valor do primeiro segmento: '))
r2 = int(input('Valor do segundo segmento: '))
r3 = int(input('Valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo', end=' ')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos acima não podem formar um triângulo!')
