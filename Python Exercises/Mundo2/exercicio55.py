# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi
# o maior e o menor peso.

maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Digite o peso da pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior}.')
print(f'O menor peso é {menor}.')