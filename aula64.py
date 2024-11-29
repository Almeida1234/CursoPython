import random
import sys

for cpfs in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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

    cpf_gerado = nove_digitos + str(resultado_digito1) + str(resultado_digito2)

    print(f' O CPF foi gerado: {cpf_gerado}')

