# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) #soma, pois são números Inteiros (int)
print( 'a' + 'b') #concatena (Junta), pois são caracteres (str)
print(type(int('1')), type(int('1')))
print(type('1'), type(int('1'))) #quando incluimos o int, string, float na frente ele faz a conversão
print(int('1') + 1)
print(float('1') + 1)
print(bool('')) #uma string vazia é considerada false
print(str(11) + 'b', 'b')