"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Não vou mostrar do 10 ao 27.')
        continue

    print(f'o contador está no numero: {contador}')
    
    if contador == 40:
        break

print('Acabou')