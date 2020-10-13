# Faça um programa que leia uma frase pelo teclado e mostre:
"""
> Quantas vezes a letra 'a' aparece;
> Em que posição ela aparece a primeira vez;
> Em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ')

print(f'A letra "a" aparece {frase.count("a")} vezes.')
print(f'O primeiro "a" aparece na posição {frase.find("a") + 1}.')
print(f'O último "a" aparece na posição {frase.rfind("a") + 1}.')
