# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada km acima do limite.
radar = 'Radar eletrônico!'
print('-' * len(radar))
print(radar)
print('-' * len(radar))

velocidade = int(input('Velocidade do carro: '))
if velocidade > 80:
    multa = float((velocidade - 80) * 7)
    print(f'Velocidade = {velocidade}km/h.')
    print(f'Você ultrapassou o limite de 80km/h, sua multa será de R${multa:.2f}!')
else:
    print(f'Velocidade = {velocidade}km/h.')
    print(f'Faça uma boa viagem!')
