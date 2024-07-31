from operacoes import calcular_media, verificar_reprovacao, relatorio_reprovacao, relatorio_completo

def inicializar_cadastro():
    """Inicializa o cadastro de alunos com nomes e matrículas."""
    nomes = ('Maria', 'Ana', 'João', 'Agatha', 'Joaquin', 'Felix')  # Tupla com nomes
    matriculas = (26, 101, 13, 37, 72, 5)  # Tupla com matrículas
    cadastro = dict(zip(matriculas, nomes))  # Dicionário associando matrículas a nomes
    return cadastro

def inicializar_notas():
    """Inicializa as notas por bimestre associadas a cada matrícula."""
    notas_primeiro_bimestre = {
        26: 7,
        101: 5,
        13: 8,
        37: 4,
        72: 7,
        5: 9
    }
    
    notas_segundo_bimestre = {
        26: 6,
        101: 4,
        13: 7,
        37: 5,
        72: 7,
        5: 8
    }
    
    notas_terceiro_bimestre = {
        26: 5,
        101: 6,
        13: 7,
        37: 6,
        72: 8,
        5: 10
    }
    
    notas_quarto_bimestre = {
        26: 8,
        101: 7,
        13: 8,
        37: 5,
        72: 6,
        5: 9
    }
    
    return {
        'primeiro': notas_primeiro_bimestre,
        'segundo': notas_segundo_bimestre,
        'terceiro': notas_terceiro_bimestre,
        'quarto': notas_quarto_bimestre
    }

def atualizar_dados_alunos(cadastro, notas):
    """Atualiza os dados dos alunos com suas notas e calcula a média final."""
    dados_alunos = {}
    
    for matricula, nome in cadastro.items():
        notas_aluno = [
            notas['primeiro'].get(matricula, 0),
            notas['segundo'].get(matricula, 0),
            notas['terceiro'].get(matricula, 0),
            notas['quarto'].get(matricula, 0)
        ]
        media = calcular_media(notas_aluno)
        dados_alunos[matricula] = {
            'nome': nome,
            'notas': notas_aluno,
            'media': media
        }
    
    return dados_alunos

def main():
    """Função principal para executar o programa."""
    cadastro = inicializar_cadastro()
    notas = inicializar_notas()
    dados_alunos = atualizar_dados_alunos(cadastro, notas)
    
    # Conjunto de matrículas para possível adição e verificação
    conjunto_matriculas = set(cadastro.keys())
    
    # Adicionar novas matrículas, se necessário
    novas_matriculas = {999}  # Exemplo de novas matrículas
    conjunto_matriculas.update(novas_matriculas)
    
    # Adicionar novas notas, se necessário
    notas['primeiro'][999] = 8
    notas['segundo'][999] = 7
    notas['terceiro'][999] = 6
    notas['quarto'][999] = 7

    # Atualizar cadastro com novas matrículas
    cadastro[999] = 'Novo Aluno'
    dados_alunos = atualizar_dados_alunos(cadastro, notas)
    
    # Verificar reprovação
    matriculas_reprovados = {matricula for matricula, dados in dados_alunos.items() if verificar_reprovacao(dados['media'])}
    
    # Gerar e exibir relatório dos alunos reprovados
    relatorio_reprovacao_resultado = relatorio_reprovacao(dados_alunos, matriculas_reprovados)
    print("Relatório dos Alunos Reprovados:")
    for linha in relatorio_reprovacao_resultado:
        print(linha)
    
    # Gerar e exibir relatório completo com todas as médias e status
    print("\nRelatório Completo:")
    relatorio_completo_resultado = relatorio_completo(dados_alunos)
    for linha in relatorio_completo_resultado:
        print(linha)

if __name__ == "__main__":
    main()
