# Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
# até ter um valor correto.

sexo = input('Informe seu sexo: [M/F] ').upper()
while sexo not in 'MF':
    sexo = input('Informe seu sexo: [M/F] ').upper()
print(f'Sexo {sexo} registrado com sucesso!')