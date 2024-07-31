# Criação do dicionário inicial
dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

# Adicionando novos elementos ao dicionário usando o método 'update'
dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'argentina'}
})

# Imprimindo o dicionário atualizado
print("Dicionário atualizado:", dicionario)

# Criando uma cópia do dicionário usando o método 'copy'
dicionario_copia = dicionario.copy()

# Removendo um elemento do dicionário original usando o método 'pop'
removido = dicionario.pop(1)  # Remove o elemento com chave 1
print("Dicionário após pop (elemento removido):", dicionario)
print("Elemento removido:", removido)

# Removendo o último elemento do dicionário usando o método 'popitem'
removido_ultimo = dicionario.popitem()  # Remove o último elemento
print("Dicionário após popitem (último elemento removido):", dicionario)
print("Elemento removido:", removido_ultimo)

# Removendo todos os elementos dos dois dicionários usando o método 'clear'
dicionario.clear()
dicionario_copia.clear()

print("Dicionário original após clear:", dicionario)
print("Dicionário cópia após clear:", dicionario_copia)

# Definindo um novo dicionário usando o método 'fromkeys'
novos_dicionario = dict.fromkeys(['a', 'b', 'c'], 'valor_default')

# Imprimindo o conteúdo do novo dicionário usando o método 'items'
print("Conteúdo do novos_dicionario usando 'items':", novos_dicionario.items())

# Imprimindo apenas as chaves do novo dicionário usando o método 'keys'
print("Chaves do novos_dicionario usando 'keys':", novos_dicionario.keys())

# Imprimindo apenas os valores do novo dicionário usando o método 'values'
print("Valores do novos_dicionario usando 'values':", novos_dicionario.values())
