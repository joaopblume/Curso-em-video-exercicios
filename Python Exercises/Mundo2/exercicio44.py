# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
# preço normal e condição de pagamento.

"""
> À vista dinheiro/cheque: 10% de desconto.
> À vista no cartão: 5% de desconto.
> Em até 2x no cartão: preço normal.
> 3x ou mais no cartão: 20% de juros.
"""

print('=' * 5, 'LOJAS BLUME', '=' * 5)
compras = float(input('Valor total das compras: R$'))
print('COMO DESEJA PAGAR?')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] Até 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
escolha = int(input('Sua opção: '))

if escolha == 1:
    final = compras - (compras / 100 * 10)
    print(f'Desconto de 10%, o valor foi de R${compras:.2f} para R${final:.2f}.')
elif escolha == 2:
    final = compras - (compras / 100 * 5)
    print(f'Desconto de 5%, o valor foi de R${compras:.2f} para R${final:.2f}.')
elif escolha == 3:
    parcela = compras / 2
    print(f'O valor das parcelas ficou definido em 2x de R${parcela:.2f}.')
else:
    vezes = int(input('Em quantas vezes deseja pagar?: '))
    final = compras + (compras / 100 * 20)
    parcela = compras / vezes
    print(f'O valor das parcelas ficou definido em {vezes}x de R${parcela:.2f},'
          f'com 20% de juros, Totalizando R${final:.2f}.')
