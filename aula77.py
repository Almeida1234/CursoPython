# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')


qtd_acertos = 0
qtd_erros = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')
    print()

    opcoes = pergunta['Opções']
    print('Opções:')
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)
        if escolha_int >= 0 and escolha_int < 4:
            if opcoes[escolha_int] == pergunta['Resposta']:
                print('Acertou')
                qtd_acertos += 1
                print()
            else:
                print('Errou')
                qtd_erros += 1
                print()
        else:
            print('Você precisa escolher a opção de 0 à 3')
            print('Errou')
            qtd_erros += 1
            print()
    else: 
        print('Escolha invalida!')
        print('Errou')
        qtd_erros += 1
        print()

print(f'Você "ACERTOU": {qtd_acertos} e "ERROU": {qtd_erros}' \
      f' de um total de {len(perguntas)} perguntas')
