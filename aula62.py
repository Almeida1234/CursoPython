"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007' 74682489070 11919827005  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '11919827005'
nove_digitos = cpf[0:9]
contagem_regressiva1 = 10
resultado_soma_digito1 = 0
resultado_digito1 = 0

for digito1 in nove_digitos:
    digito_multiplicado = int(digito1) * contagem_regressiva1
    resultado_soma_digito1 += digito_multiplicado
    contagem_regressiva1 -= 1

resultado_multiplicado = resultado_soma_digito1 * 10
resto_divisao = resultado_multiplicado % 11

resultado_digito1 = resto_divisao if resto_divisao <= 9 else 0

dez_digito = nove_digitos + str(resultado_digito1)
contagem_regressiva2 = 11
resultado_soma_digito2 = 0
resultado_digito2 = 0

for digito2 in dez_digito:
    digito_multiplicado2 = int(digito2) * contagem_regressiva2
    resultado_soma_digito2 += digito_multiplicado2
    contagem_regressiva2 -= 1

resultado_multiplicado2 = resultado_soma_digito2 * 10
resto_divisao2 = resultado_multiplicado2 % 11

if resto_divisao2 <= 9:
    resultado_digito2 = resto_divisao2
else:
    resto_divisao2 = 0
    resultado_digito2 = resto_divisao2

cpf_completo = nove_digitos + str(resultado_digito1) + str(resultado_digito2)

if cpf == cpf_completo:
    print(f'O CPF: {cpf} é válido')
else:
    print(f'O CPF: {cpf} é inválido')



# cpf_enviado_usuario = '74682489070'
# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')



# cpf_enviado_usuario = '74682489070'
# nove_digitos = cpf_enviado_usuario[:9]

# # Cálculo do primeiro dígito verificador
# contador_regressivo_1 = 10
# resultado_digito_1 = 0
# i = 0  # Usando um índice para percorrer os dígitos

# while contador_regressivo_1 > 1:  # Vai até o número 2, pois o contador vai de 10 até 2
#     resultado_digito_1 += int(nove_digitos[i]) * contador_regressivo_1
#     contador_regressivo_1 -= 1
#     i += 1

# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# # Cálculo do segundo dígito verificador
# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11
# resultado_digito_2 = 0
# i = 0  # Resetando o índice para percorrer novamente os dígitos

# while contador_regressivo_2 > 1:  # Vai até o número 2, pois o contador vai de 11 até 2
#     resultado_digito_2 += int(dez_digitos[i]) * contador_regressivo_2
#     contador_regressivo_2 -= 1
#     i += 1

# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# # Gerando o CPF
# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# # Validação do CPF
# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')