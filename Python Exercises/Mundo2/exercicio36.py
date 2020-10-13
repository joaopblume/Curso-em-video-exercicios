# Escreva um programa para aprovar um empréstimo bancário para o comprador de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode execeder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Em quantos anos será paga a casa: '))
prestacao = casa / (anos * 12)
minimo = salario / 100 * 30

if prestacao > minimo:
    print(f'Empréstimo NEGADO! A prestação excedeu 30% do salário do comprador.')
else:
    print(f'Empréstimo APROVADO! A casa com valor de R${casa:.2f}, '
          f'será paga em {anos} anos, com prestações de R${prestacao:.2f} mensais.')
