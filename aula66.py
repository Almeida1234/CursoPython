"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
# def multiplo(numero, multiplo):
#     resultado = numero % multiplo == 0
#     print(f'{numero} é múltiplo {multiplo}', end=' ')
#     print(resultado)

# multiplo(16, 8)
# multiplo(15, 3)
# multiplo(10, 2)

def soma(x, y, z):
    # Definição
    print(f'{x=} + y={y} = {x + y}')
    print(f'{x=} + y={y} +z={z}', '|', 'x + y + z =', x + y + z) 


soma(1, 2, 3)
soma(y=1, z=2, x=2)

print(1, 2, 3, sep='-')