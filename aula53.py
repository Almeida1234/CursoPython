"""
enumerate - enumera iteráveis (índices)
"""

"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append ('Cecilia')
lista.pop()
lista.insert (0, 'Ricardo')
lista.append ('Cecilia')

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# print(next(lista_enumerada))
# print(next(lista_enumerada))
# print(lista)

# for item in lista_enumerada:
for item in enumerate(lista):
    print(item)

for indices, nome in enumerate(lista):
    print(indices, nome, lista[indices])

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')


# indice = 0
# while indice < len(lista):
#     nome = lista[indice]
#     print(indice, nome)
#     indice += 1