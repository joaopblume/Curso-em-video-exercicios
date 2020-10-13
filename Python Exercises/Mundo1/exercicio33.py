# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

menor = 2
if num1 < num2 and num1 < num3:
    menor = num1
elif num3 < num2 and num3 < num1:
    menor = num3

print(f'Entre os números {num1}, {num2} e {num3}...')
print(f'O maior número é {maior}, e o menor número é {menor}!')