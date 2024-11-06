# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar ou [S]air: ')
# print(entrada)
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') or senha_digitada == senha_permitida:
#    print('Entrar')
# else:
#    print('Sair')

# Avaliação de curto circuito
# senha = 0 or False or 0 or 'abc'
senha = input('Senha: ') or 'Sem senha'
print(senha)
print(True or 1 or True)
print(bool(''))