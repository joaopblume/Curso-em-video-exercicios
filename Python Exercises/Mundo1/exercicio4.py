# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ela.

caractere = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(caractere)}')
print(f'Só tem espaços? {caractere.isspace()}')
print(f'É um número? {caractere.isnumeric()}')
print(f'É alfabético? {caractere.isalpha()}')
print(f'É alfanumérico? {caractere.isalnum()}')
print(f'Está em maiúsculo? {caractere.isupper()}')
print(f'Está em minúsculo? {caractere.islower()}')
print(f'É um capitalizado? {caractere.istitle()}')
