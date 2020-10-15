# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
"""
> A média de idade do grupo;
> Qual o nome do homem mais velho;
> Quantas mulheres tem menos de 20 anos.
"""

somaidades = 0
nomevelho = ''
idadevelho = 0
menosdevinte = 0

for p in range(1, 5):
    print(f'=== Pessoa {p} ===')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    somaidades += idade
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        menosdevinte += 1
mediafinal = somaidades / 4
print(f'A média da idade do grupo é de {mediafinal}')
print(f'O homem mais velho tem {idadevelho} anos e se chama {nomevelho}.')
print(f'Ao todo são {menosdevinte} mulheres com menos de 20 anos.')
