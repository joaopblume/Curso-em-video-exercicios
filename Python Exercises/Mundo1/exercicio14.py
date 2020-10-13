# Escreva um programa que converta uma temperatura digitada em °C para °F.

celsius = float(input('Temperatura em °C: '))
farenheit = ((9 * celsius) / 5) + 32

print(f'A temperatuda de {celsius}°C corresponde a {farenheit}°F.')
