# Desenvolva uma lógica que leia o peso e a aultura de uma pessoa, calcule seu IMC,
# e mostre seu status de acordo com a tabela abaixo:
"""
> Abaixo de 18.5 = Abaixo do peso
> Entre 18.5 a 25 = Peso ideal
> Entre 25 a 30 = Sobrepeso
> Entre 30 a 40 = Obesidade
> Acima de 40 = Obesidade Mórbida
"""

peso = float(input('Digite seu peso atual (kg): '))
altura = float(input('Digite sua altura atual (m): '))
imc = peso / (altura ** 2)

print(f'O seu IMC é de {imc:.1f}.')

if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc <= 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
