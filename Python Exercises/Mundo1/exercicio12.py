# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto: R$'))
desc = preco - (preco * 0.05)
print(f'O preço que antes era R${preco}, com desconte de 5% agora é de R${desc:.2f}!')
