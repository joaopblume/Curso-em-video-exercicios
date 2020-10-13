# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Salário do funcionário: R$'))
aumento = salario + (salario * 15 / 100)
print(f'O salário que antes era R${salario:.2f}, com um aumento de 15% agora passa ser de R${aumento:.2f}!')
