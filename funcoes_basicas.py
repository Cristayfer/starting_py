# ==============================
# EXEMPLO DE FUNÇÕES BÁSICAS EM PYTHON
# ==============================

# 1️⃣ print() — exibe algo na tela
print("Olá, mundo!")  # Mostra texto no console

# 2️⃣ input() — lê uma entrada do usuário
nome = input("Digite seu nome: ")  # Armazena o texto digitado na variável 'nome'

# 3️⃣ int(), float(), str() — convertem tipos de dados
idade = int(input("Digite sua idade: "))  # Converte o valor digitado (texto) para número inteiro
altura = float(input("Digite sua altura: "))  # Converte para número decimal (float)

# 4️⃣ type() — mostra o tipo de um valor ou variável
print("O tipo de 'idade' é:", type(idade))
print("O tipo de 'altura' é:", type(altura))

# 5️⃣ len() — retorna o tamanho (quantidade de caracteres ou itens)
print("Seu nome tem", len(nome), "letras.")

# 6️⃣ Funções matemáticas básicas com operadores
soma = idade + 5
divisao = altura / 2
print("Daqui a 5 anos, você terá", soma, "anos.")
print("Sua altura dividida por 2 é", divisao)

# 7️⃣ if / elif / else — decisões lógicas
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é adolescente.")
else:
    print("Você é criança.")

# 8️⃣ Função personalizada (def) — cria sua própria função
def saudacao(pessoa):
    print("Olá,", pessoa, "! Seja bem-vindo(a)!")

# Chamando (executando) a função
saudacao(nome)

# 9️⃣ range() e for — repetição
print("Contando até 5:")
for numero in range(1, 6):
    print(numero)

# 1️⃣0️⃣ lista (list) — estrutura para guardar vários valores
frutas = ["maçã", "banana", "laranja"]
print("Minhas frutas favoritas são:", frutas)
print("A primeira fruta da lista é:", frutas[0])

# 1️⃣1️⃣ append() — adiciona item na lista
frutas.append("uva")
print("Lista atualizada:", frutas)