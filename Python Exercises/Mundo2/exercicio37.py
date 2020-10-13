# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão:
"""
> 1 para binário
> 2 para octal
> 3 para hexadecimal
"""

num = int(input('Escolha um número para ser convertido: '))

print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

choice = int(input('Sua opção: '))
if choice == 1:
    print(f'{num} convertido para BINÁRIO fica {bin(num)[2:]}!')
elif choice == 2:
    print(f'{num} convertido para OCTAL fica {oct(num)[2:]}!')
elif choice == 3:
    print(f'{num} convertido para HEXADECIMAL fica {hex(num)[2:]}!')
else:
    print('Opção inválida, tente novamente.')
