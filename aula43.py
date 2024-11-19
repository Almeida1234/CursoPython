texto = 'Python'
i = 0 
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra, i)
    i += 1
print(novo_texto + '*')


# texto = 'Python'

# i = 0
# tamanho_string = len(texto)
# texto_atual = ''

# while i < tamanho_string:
#     print(texto[i], i)
#     texto_atual += texto[i]
        
#     i += 1
# print(f'{texto=} = {texto_atual=}')

#Outro código
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print('Aquele laço acima pode ter repetições infinitas.')