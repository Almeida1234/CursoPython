"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel =}')
print(f'{variavel:->10}.') # Esquerda
print(f'{variavel:$<10}.') # Direita
print(f'{variavel:*^11}') # Centraliza
print(f'{1000.4873648123746:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')