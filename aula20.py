primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

resultado = primeiro_valor >= segundo_valor
print('O primeiro número é maior que o segundo: ', resultado)

if primeiro_valor >= segundo_valor:
    print('Sim o primeiro valor:', type(int(primeiro_valor)), 'é maior ou igual o segundo valor:', segundo_valor)
    print(f'Sim o primeiro valor: {primeiro_valor} é maior ou igual o segundo valor: {segundo_valor} ')
    print(f'{primeiro_valor} é maior ou igual o {segundo_valor}')

else:
    print('Não o primeiro valor:', primeiro_valor, 'é menor que o segundo:', segundo_valor)
    print(f'Não o primeiro valor: {primeiro_valor} é menor que o segundo valor: {segundo_valor}')
    print(f'{segundo_valor} é maior do que o {primeiro_valor}')