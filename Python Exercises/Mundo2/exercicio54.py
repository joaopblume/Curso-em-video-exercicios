# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for n in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {n}ª pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo temos {totmaior} pessoas maiores de idade, e {totmenor} pessoas menores de idade.')
