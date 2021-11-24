nome = 'Brunno'
print(nome, type(nome))
idade = 33
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / altura ** 2

print('Nome: ', nome)
print('Altura: ', altura)
print('Idade: ', idade)
print('Maior que 18 anos?: ', e_maior)

print(nome, 'têm', idade, 'anos de idade e seu imc é', imc, '.')
print(f'{nome} têm {idade} anos de idade e seu imc é {imc:.2f}.')
print('{} têm {} anos de idade e seu imc é {:.2f}.'.format(nome, idade, imc))
print('{0} têm {1} anos de idade e seu imc é {2:.2f}.'.format(nome, idade, imc))
print('{n} têm {i} anos de idade e seu imc é {im:.2f}.'.format(n=nome, i=idade, im=imc))
