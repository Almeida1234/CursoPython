"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante   '
lista_frases_crua = frase.split(', ')
lista_frases = []
print(lista_frases_crua)

for i, frase in enumerate(lista_frases_crua):
    # strip corta os espaços do começo e fim rstrip da direita e lstrip da esqueda
    lista_frases.append(lista_frases_crua[i].strip())
    print(i, frase.strip())
lista_frases.append ('!')
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)