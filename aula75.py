# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

numero = input('Digite um numero: ')
if numero.isdigit():
    numero = int(numero)
    opcao = input('o que deseja fazer com o número: [D}uplicar, [T]riplicar, [Q]uadruplicar: ').lower()
    if opcao == 'd' or opcao.startswith('duplicar'):
        print(duplicar(numero))
    elif opcao == 't' or opcao.startswith('triplicar'):
        print(triplicar(numero))
    elif opcao == 'q' or opcao.startswith('quadruplicar'):
        print(quadruplicar(numero))
    else:
        print('Não digitou nenhuma opção válida!')
else:
    print('Você não digitou um número válido!')