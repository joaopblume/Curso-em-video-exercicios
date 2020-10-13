# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ela ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo
# do alistamento. Seu programa deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print(f'Você nasceu em {ano}, em {date.today().year} tens {idade} anos.')
    print(f'Ainda faltam {18 - idade} anos para seu alistamento.')
    print(f'Seu alistamento será em {ano + 18}.')
elif idade == 18:
    print(f'Você nasceu em {ano}, em {date.today().year} tens {idade} anos.')
    print(f'Você deve se alistar IMEDIATAMENTE!')
else:
    print(f'Você nasceu em {ano}, em {date.today().year} tens {idade} anos.')
    print(f'Você deveria ter se alistado a {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano + 18}!')
