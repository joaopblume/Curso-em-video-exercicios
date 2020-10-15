# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade.
"""
> Até 9 anos: MIRIM
> Até 14 anos: INFANTIL
> Até 19 anos: JÚNIOR
> Até 25 anos: SÊNIOR
> Acima: MASTER
"""

from datetime import date

nasc = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos, sua categoria é MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos, sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos, sua categoria é JÚNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos, sua categoria é SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos, sua categoria é MASTER.')
