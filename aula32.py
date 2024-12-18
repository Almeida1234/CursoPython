"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')


numero = input('Digite um número: ')

try:
    entrada_int = float(numero)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

print(f'\n')
print(f"-" * 20)
print(f'\n')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('que horas são: ')
try:
    hora_int = int(hora)
    
    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print(f'Boa tarde')
    elif hora_int >=18 and hora_int <= 23:
        print(f'Boa noite')
    else:
        print(f'Você informou um horário invalido')
    
except:
    print(f'Por favor, digite apenas números inteiros')

print(f'\n')
print(f'-' * 20)
print(f'\n')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
numero = input('Escreva seu primeiro nome: ')
nome = len(numero)

if nome > 1 and nome < 5:
    print(f'Seu nome é curto')
elif nome > 4 and nome < 7:
    print(f'Seu nome é normal')
elif nome > 6:
    print(f'Seu nome é muito grande')
else:
    print(f'Digite um nome valido')


nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')