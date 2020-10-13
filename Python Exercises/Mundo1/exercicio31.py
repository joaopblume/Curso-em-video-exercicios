# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando 0,50 por km para viagens
# de até 200km e 0,45 para viagens mais longas.

dist = int(input('Distância da viagem em km: '))
if dist > 200:
    preco = dist * 0.45
    print(f'O preço para uma viagem de {dist}km é de R${preco}!')
else:
    preco = dist * 0.50
    print(f'O preço para uma viagem de {dist}km é de R${preco}!')
