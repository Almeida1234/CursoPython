"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2          3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40), ], # 2

]

#print(salas[2][3][3])

for numero, sala in enumerate(salas):
    print(f'A Sala {numero} tem esses alunos = {sala}')
    for numero1, alunos in enumerate(sala):
        print(f'Aluno {numero1}: {alunos}')
        
        

# sala = 0
# while sala < len(salas):
#     salass = salas[sala]
#     print(f'A Sala {sala} tem esses alunos = {salass}')
    
#     alunos = 0
#     while alunos < len(salass):
#         print(f'Aluno {alunos}:{salass[alunos]}')
#         alunos += 1
    
#     sala += 1