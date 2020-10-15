# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Escolha um número para ver seu FATORIAL: '))
cont = num
fat = 1
while cont > 0:
    print(cont, end='')
    if cont > 1:
        print(' x', end=' ')
    else:
        print(' =', end=' ')
    fat *= cont
    cont -= 1

print(fat)
