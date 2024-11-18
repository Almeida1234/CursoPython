""" Calculadora com while """

while True:
    numero_1 = input('Digite um numero: ')
    operador = input('Digite o operador (+-/*): ')
    numero_2 = input('Digite outro numero: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')



    sair = input('Você quer sair do programa? digite: [S]sim ou [N]não: ').lower().startswith('s')
    print('\n')
    if sair is True:
        break


# meu código Funciona kkkkk
# while True:
#     primeiro_numero = input('Digite o primeiro numero: ')
#     operadores = input('Digite um operador +, -, *, /: ')
#     segundo_numero = input('Digite o segundo numero: ')
    
#     try:
#         if primeiro_numero and segundo_numero:
#             float_num1 = float(primeiro_numero)
#             float_num2 = float(segundo_numero)

#             if operadores == '+':
#                 print(f'A soma é: {float_num1 + float_num2}')

#             elif operadores == '-':
#                 print(f'A subtração é: {float_num1 - float_num2}')

#             elif operadores == '*':
#                 print(f'A multiplicação é: {float_num1 * float_num2}')

#             elif operadores == '/':
#                 print(f'A divisão é: {float_num1 / float_num2}')

#             else:
#                 print(f'Você não digitou os operadores validos "+", "-", "*", "/"')

#     except:
#         print('Você digitou Letras, precisa digitar números!')

#     print(f'{'-'*20}\n')
#     sair = input('Você quer sair do programa? digite: [S]sim ou [N]não: ').lower().startswith('s')
#     print('\n')
#     if sair is True:
#         break