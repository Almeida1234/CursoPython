a = 'Ricardo'
b = 'Almeida'
c = 1.1
string = 'a={nome1} a={nome1} b={nome2} c={nome3:.1f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)