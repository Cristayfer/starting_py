nome = 'Cristayfer de Araújo'
altura = 1.77
peso = 64
imc = peso / altura ** 2

#Formatação de strings
"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é:'
linha_3 = f'{imc:.10f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Cristayfer tem 1.77 de altura
# pesa 65 quilos e seu imc é
# 20.428357113217785
