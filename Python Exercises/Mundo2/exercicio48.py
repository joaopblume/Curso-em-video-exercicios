# Faça um programa que calcule a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

cont = 0
soma = 0

for num in range(1, 501, 2):
    if num % 3 == 0:
        cont += 1
        soma += num
print(f'Em {cont} números ímpares múltiplos de 3, a soma é de {soma}.')
