# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

num = randint(0, 5)
escolha = int(input('Tente descobrir o número que o computador pensou entre 0 e 5:  '))
if escolha == num:
    print(f'Você acertou, o número correto é {num}!')
else:
    print(f'Você errou, o número correto era {num}!')
