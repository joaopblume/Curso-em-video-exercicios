# Faça um programa que leia o nome completo de uma pessoa.
# Mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome: ').strip()
separado = nome.split()

print(f'Muito prazer em te conhecer {nome}!')
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu último nome é {separado[-1]}')
