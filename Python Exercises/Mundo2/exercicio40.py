# Crie um programa que leia duas notas de um aluno e calcula sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
"""
> Média abaixo de 5.0 = REPROVADO
> Média entre 5.0 e 6.9 = RECUPERAÇÃO
> Média acima de 7.0 = APROVADO
"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'A média do aluno foi {media}. APROVADO!')
elif 5 <= media < 7:
    print(f'A média do aluno foi {media}. RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi {media}. REPROVADO!')
