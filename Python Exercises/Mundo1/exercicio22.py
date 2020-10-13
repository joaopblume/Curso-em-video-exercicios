# Crie um programa que leia o nome completo de uma pessoa e mostre:
"""
> O nome com todas as letras maiúsculas e minúsculas
> Quantas letras ao todo (sem considerar espaços)
> Quantas letras tem o primeiro nome
"""

nome = input('Digite um nome: ').strip()
print('Analisando nome ...')
print(f'Seu nome em maiúsculo fica: {nome.upper()}')
print(f'Seu nome em minúsculo fica: {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome {nome.find(" ")} letras.')
