# Melhore o jogo do exercício 28 onde o computador vai "pensar" em um número entre 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
contador = 0
computador = randint(0, 10)
jogador = int(input('Tente adivinhar o número que o computador pensou entre 0 e 10: '))
while jogador != computador:
    print('Você errou!')
    jogador = int(input('Tente adivinhar o número que o computador pensou entre 0 e 10: '))
    contador += 1
print(f'Você acertou o número {computador}, em {contador} tentativas.')
