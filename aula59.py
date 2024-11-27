# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2          3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40), ], # 2

]

# a, b, c, *_, u = lista
# print(a,c,u)

print(*lista) # traz tudo que tem dentro da lista
print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(lista) 
print(*string)
print(*tupla)
print(salas)

for nome in lista:
    print(nome, end=' ')# end está fazendo ficar tudo na mesma linha, separando por espaço
print('\n', *salas, sep='\n')
