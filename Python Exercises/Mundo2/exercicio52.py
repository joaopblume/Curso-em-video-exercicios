# Faça um programa que leia um número interio e diga se ele é ou não um número primo.
total = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[31m', end=' ')
        total += 1
    else:
        print(f'\033[33m', end=' ')
    print(f'{c}', end=' ')
print()
print(f'O número {num} foi divisível {total} vezes.', end=' ')
if total == 2:
    print('É primo!')
else:
    print('NÃO é primo!')