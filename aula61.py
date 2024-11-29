"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70 / 119.198.270-05
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '11919827005'
nove_digitos = cpf[0:9]
contagem_regressiva = 10
resultado_soma_digito = 0

for digito in nove_digitos:
    digito_multiplicado = int(digito) * contagem_regressiva
    resultado_soma_digito += digito_multiplicado
    contagem_regressiva -= 1

resultado_multiplicado = resultado_soma_digito * 10
resto_divisao = resultado_multiplicado % 11

if resto_divisao <= 9:
    print(resto_divisao)
else:
    resto_divisao = 0
    print(resto_divisao)



# codigo professor
# cpf = '74682489070'
# nove_digitos = cpf[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito_1 in nove_digitos:
#     resultado_digito_1 += int(digito_1) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)