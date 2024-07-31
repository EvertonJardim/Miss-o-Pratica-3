# Criação do set 'set_inicial'
set_inicial = {11, 12, 13, 14}

# Imprimindo o conteúdo inicial do set
print("Conteúdo inicial do set_inicial:", set_inicial)

# Adicionando o elemento 15 ao set usando o método 'add'
set_inicial.add(15)

# Imprimindo o conteúdo do set após o 'add'
print("Conteúdo após add:", set_inicial)

# Atualizando o set com novos elementos usando o método 'update'
set_inicial.update({1, 2, 3, 4, 5})

# Imprimindo o conteúdo do set após o 'update'
print("Conteúdo após update:", set_inicial)

# Removendo o elemento 13 do set usando o método 'discard'
set_inicial.discard(13)

# Imprimindo o conteúdo do set após o 'discard'
print("Conteúdo após discard:", set_inicial)

# Criando um novo set 'novo_set'
novo_set = set([20, 21, 23, 1, 2])

# Imprimindo o conteúdo do novo set
print("Conteúdo do novo_set:", novo_set)

# Imprimindo o resultado da união entre os dois sets
uniao = set_inicial.union(novo_set)
print("União entre set_inicial e novo_set:", uniao)

# Imprimindo o resultado da interseção entre os dois sets
interseccao = set_inicial.intersection(novo_set)
print("Interseção entre set_inicial e novo_set:", interseccao)

# Imprimindo o resultado da diferença entre os dois sets
diferenca = set_inicial.difference(novo_set)
print("Diferença entre set_inicial e novo_set:", diferenca)

# Imprimindo o resultado da diferença simétrica entre os dois sets
diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre set_inicial e novo_set:", diferenca_simetrica)


