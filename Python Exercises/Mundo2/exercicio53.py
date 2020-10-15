# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
"""
ex:
- apos a sopa
- a sacada da casa
- a torre da derrota
- o lobo ama o bolo
- anotaram a data da maratona
"""

frase = input('Digite um frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
