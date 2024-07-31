# Criação do dicionário 'meu_dicionario'
meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}

# Imprimindo o conteúdo do dicionário
print("Conteúdo do meu_dicionario:", meu_dicionario)

# Imprimindo o tipo de dados do dicionário
print("Tipo de dados do meu_dicionario:", type(meu_dicionario))

# Imprimindo o valor da chave 1 usando o método 'get'
# Note que 'get' precisa da chave para buscar o valor correto
print("Valor da chave 1:", meu_dicionario.get(1))

# Imprimindo o tamanho do dicionário
print("Tamanho do meu_dicionario:", len(meu_dicionario))

# Criação do novo dicionário aninhado 'dicionario_frutas'
dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})

# Imprimindo os valores das chaves "nome" e "tipo" da chave 1
print("Chave 1 - Nome:", dicionario_frutas[1]["nome"])
print("Chave 1 - Tipo:", dicionario_frutas[1]["tipo"])

# Imprimindo os valores das chaves "nome" e "tipo" da chave 2
print("Chave 2 - Nome:", dicionario_frutas[2]["nome"])
print("Chave 2 - Tipo:", dicionario_frutas[2]["tipo"])

# Iterando no dicionário 'dicionario_frutas' e imprimindo os valores das chaves "nome" e "tipo"
print("Valores de todas as chaves 'nome' e 'tipo' em dicionario_frutas:")
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")
