# # Exercícios com funções

# # Crie uma função que multiplica todos os argumentos
# # não nomeados recebidos
# # Retorne o total para uma variável e mostre o valor
# # da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3)
print(multiplicação)



# # Crie uma função fala se um número é par ou ímpar.
# # Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)



# Meu Código:
# def par_impar(numer):
#     entrada = input('Digite uma valor: ')
#     if entrada.isdigit():
            
#         if int(entrada) % 2 == 0:
#             return f'O número {entrada} é Par'
#         else:
#             return f'O número {entrada} é Ímpar'
#     else:
#         return 'Você não digitou um número!'

    
# resultado = par_impar(None)
# print(resultado)


# # def par_impar(numero):
# #     if numero % 2 == 0:
# #         return f'O número {numero} é Par'
# #     else:
# #         return f'O número {numero} é Ímpar'
        
# # resultado = par_impar(3)
# # print(resultado)
# # resultado = par_impar(4)
# # print(resultado)
