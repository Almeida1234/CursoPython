"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
"""
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
append, insert, pop, del, clear, extend, +
create, read, update, delete
"""

lista_a = ['Ricardo', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
lista_c = [123, 456]
lista_d = [789]
Lista_concate = lista_c + lista_d
Lista_concate1 = lista_c.extend(lista_d)
lista_a[0] = 'Ricardo Lindão'
lista_bb = lista_b[0]
del lista_a[3]
lista_a.append(50) # adiciona no final
lista_a.pop() # remove o ultimo da lista
lista_a.append(60) # adiciona no final
lista_a.append(70) # adiciona no final
lista_a.pop() # remove o ultimo da lista
ultimo_valor = lista_a.pop(3)
del lista_a[-1]
lista_a.insert(0, 5)
print(lista_a)
print(lista_b)
print(lista_bb)
print(lista_a, 'Removida', ultimo_valor)
print(Lista_concate)
print(Lista_concate1)