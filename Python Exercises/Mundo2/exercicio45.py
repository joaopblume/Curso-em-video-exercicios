# Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint
from time import sleep

jokenpo = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('Suas opções: ')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Qual é sua jogada? '))
print('JO', end='')
sleep(1)
print('-KEN', end='')
sleep(1)
print('-PO!')
sleep(1)
print(f'Você jogou {jokenpo[jogador]}.')
print(f'O computador jogou {jokenpo[computador]}')

if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('Computador VENCEU!')
    else:
        print('Você VENCEU!')
elif jogador == 1:
    if computador == 0:
        print('Você VENCEU!')
    elif computador == 1:
        print('EMPATE!')
    else:
        print('Computador VENCEU!')
else:
    if computador == 0:
        print('Computador VENCEU!')
    elif computador == 1:
        print('Você VENCEU!')
    else:
        print('EMPATE!')
