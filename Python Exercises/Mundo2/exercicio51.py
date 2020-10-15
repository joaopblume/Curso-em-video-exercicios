# Desenvolva um programa que leia o primeiro termo e a razao de uma Progressão Aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.

num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
decimo = num + (10 - 1) * razao
for n in range(num, decimo + razao, razao):
    print(n, end='-')
print('Fim!')