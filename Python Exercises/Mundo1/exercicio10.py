# Crie um programa que leie quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ele pode comprar

# Considere US$1 = R$5

carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 5
print(f'Com R${carteira:.2f} você pode comprar US${dolar:.2f}!')
