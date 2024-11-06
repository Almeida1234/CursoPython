"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(len(variavel))
print(len(variavel[3:8]))
print(variavel[0:9:2])
print((variavel[0:len(variavel):1]))
print(variavel[4])
print(variavel[-4])
print(f'-' * 10)
print(variavel[4:])# para pegar o indice até o final tem que deixar vazio
print(variavel[4:8])

