"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista[1] = 'Ricardo'
lista.append ('Cecilia')
indices = range(len(lista))

for ind in indices:
    print(f'{ind} O nome: {lista[ind]} tem: {len(lista[ind])} letras {type(lista)}')

print(f'{'-' * 50}')

# Meu código for e while
i = 0
for nome in lista:
    print(f'{i} O nome: {nome} tem: {len(nome)} letras {type(nome)}')
    i += 1

print(f'{'-' * 50}')

indice = 0
while indice < len(lista):
    nome1 = lista[indice]
    print(f'{indice} O nome: {nome1} tem: {len(nome1)} letras {type(nome1)}')
    indice += 1