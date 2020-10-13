# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

medida = float(input('Digite um valor em metros: '))
cm = medida * 100
mm = medida * 1000

print(f'Valor digitado: {medida}m')
print(f'Valor em centímetros: {cm:.0f}cm')
print(f'Valor em milímetros: {mm:.0f}mm')
