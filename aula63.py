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
import re 
import sys

entrada = input('Digite um CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)

# O metodo replace é usado para substituir por outra coisa
#cpf = '340.756.708-13'.replace('.', '').replace('-', '')
# cpf = '340.756.708-13' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '') \
#     .replace('_', '') 
    
entrada_e_sequencial = entrada == entrada[0] *len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

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