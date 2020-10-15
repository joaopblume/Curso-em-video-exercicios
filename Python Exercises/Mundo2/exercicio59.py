# Crie um programa que leia dois valores e mostre um menu como o abaixo:
"""
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair
"""
# Seu programa deverá realizar a operação solicitada em cada caso.
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair')
    opcao = int(input('O que deseja fazer? '))
    if opcao == 1:
        print(f'A soma entre {num1} e {num2} = {num1 + num2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {num1} e {num2} = {num1 * num2}.')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número entre {num1} e {num2} é {maior}.')
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = (int(input('Segundo valor: ')))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')