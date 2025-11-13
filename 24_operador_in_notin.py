#Operadores in e not in
#Strings são iteráveis
# 0 1 2 3 4 5 6 7 8 9
# C r i s t a y f e r
# 0-1-2-3-4-5-6-7-8-9

nome = 'Cristayfer'

print(nome[3])
print(nome[-5])

print(10 * '-')

print('f' in nome)
print('z' in nome)

print(10 * '-')

print('fer' in nome)
print('zero' in nome)

print(10 * '-')

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')