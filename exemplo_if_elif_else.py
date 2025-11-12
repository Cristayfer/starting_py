# Pedimos ao usuário para digitar uma nota de 0 a 10
nota = float(input("Digite sua nota (0 a 10): "))

# Estrutura condicional para verificar o valor da nota

if nota >= 7:
    # Se a nota for 7 ou maior
    print("Você foi aprovado!")
elif nota >= 5:
    # Se a nota for menor que 7, mas maior ou igual a 5
    print("Você está de recuperação.")
else:
    # Se a nota for menor que 5
    print("Você foi reprovado.")