"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
""" 
# print (1234)
# print (1234)
# int('a')

numero_str = input('Vou dobrar o número que vc digitar: ')
print(f'{numero_str.isdigit()}') # isdigit verifica se o número digitado é inteiro

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro do {numero_str} é {numero_str * 2}')
#     print(f'O dobro do {numero_str} é {int(numero_str) * 2}')
#     print(f'O dobro do {numero_str} é {numero_float * 2:.3f}')
# else:
#     print(f'Isso não é um números ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'Float: {numero_float}')
#   print(f'O dobro do {numero_str} é {numero_str * 2}')
    print(f'O dobro do {numero_str} é {int(numero_str) * 2}')
    print(f'O dobro do {numero_str} é {numero_float * 2:.1f}')
except:
    print(f'Isso não é um números ')



