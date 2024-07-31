# Criação da lista 'lista_mesclada'
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Imprimindo o conteúdo da lista
print("Conteúdo inicial da lista_mesclada:", lista_mesclada)

# Adicionando o elemento ["Lista aninhada"] usando o método 'append'
lista_mesclada.append(["Lista aninhada"])

# Imprimindo o conteúdo da lista após o 'append'
print("Conteúdo após append:", lista_mesclada)

# Inserindo o elemento 5 na posição 4 usando o método 'insert'
lista_mesclada.insert(4, 5)

# Imprimindo o conteúdo da lista após o 'insert'
print("Conteúdo após insert:", lista_mesclada)

# Imprimindo o tamanho atual da lista
print("Tamanho da lista_mesclada:", len(lista_mesclada))

# Removendo o item na posição 1
del lista_mesclada[1]

# Imprimindo o conteúdo da lista após a remoção
print("Conteúdo após remoção:", lista_mesclada)

# Criando a nova lista 'nova_lista_mesclada' com itens até a posição 4 da lista original
nova_lista_mesclada = lista_mesclada[:5]

# Imprimindo o conteúdo da nova lista
print("Conteúdo da nova_lista_mesclada:", nova_lista_mesclada)
