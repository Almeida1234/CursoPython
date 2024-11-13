"""
Iterando strings com while
"""
#       012345678910 numero positivos
#nome = 'Ricardo'  # Iteráveis
#      1110987654321 numeros negativos

nome = 'Ricardo'

indice = 0
novo_nome = ''
# print(f'{nome}')
# print(f'{novo_nome}')
# print(f'{nome[3:7]}')
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
novo_nome += '*'
print(novo_nome)