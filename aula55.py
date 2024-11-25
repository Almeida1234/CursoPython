"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = decimal.Decimal(0.1)
numero_4 = decimal.Decimal(0.7)
numero_5 = numero_1 + numero_2
numero_6 = numero_3 + numero_4

print(numero_5)
print(f'{numero_5:.2f}')
print(type(round(numero_5, 2)))
print(round(numero_5, 2))
print(numero_6)
print(f'{numero_6:.2f}')
print(type(round(numero_6, 2)))
print(round(numero_6, 2))