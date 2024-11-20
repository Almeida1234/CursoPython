"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""



#Meu código
palavra_secreta = 'Cecilia'.lower()
letra_certa = ''
letra_errada = ''
contador = 0
palavra_formada = ''

while palavra_formada != palavra_secreta:
    digite_letra = input('Digite uma letra: ').lower()
    letra = digite_letra
    
    if len(letra) > 1:
        print('Você digitou mais de uma Letra.')
        continue

    if letra in palavra_secreta:
        letra_certa += letra
        contador += 1
        
        
    elif letra not in palavra_secreta:
        letra_errada += f'{letra}, '
        contador += 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')

print(f'"PARABÉNSA"' \
      f'A palavra secreta é: "{palavra_secreta}" você acertou!\n' \
      f'você tentou: {contador}X')
print(f'Essas são todoas as Letras Erradas que você digitou: " {letra_errada}"')
