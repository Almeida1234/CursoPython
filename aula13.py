nome = 'Ricardo Almeida'
altura = 1.74
peso = 95
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.3f} de altura\n'
print(linha_1)

linha_2 = f'Meu nome é: {nome} e tenho {altura:.3f} de altura'
print(linha_2)

linha_3 = f'Eu estou pesando: {peso}KL e  meu IMC é de {imc:.3f}\n'
print(linha_3)

#print(nome, altura, peso, imc)

print('Meu nome:', nome,'\n', 'Minha Altura:', altura,'\n', 
      'Meu peso:', peso,'Kl','\n', 'Minha média caorporal:', imc)

# Ricardo Almeida tem 1.74 de altura,
# pesa 95 quilos e seu IMC é 
# 31.37798916633637