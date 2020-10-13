# Faça um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salário acima de R$1250,00, Calcule um aumento de 10%,
# para inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salário do funcionário: '))
if salario <= 1250:
    aumento = salario + (salario / 100 * 15)
    print(f'Seu aumento será de 15%, sendo assim seu salário vai de R${salario:.2f} para R${aumento:.2f}!')
else:
    aumento = salario + (salario / 100 * 10)
    print(f'Seu aumento será de 10%, sendo assim seu salário vai de R${salario:.2f} para R${aumento:.2f}!')
