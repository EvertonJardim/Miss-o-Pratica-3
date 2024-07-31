def calcular_media(notas):
    """Calcula a média das notas fornecidas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """Verifica se o aluno foi reprovado com base na média."""
    return media < 6

def relatorio_reprovacao(dados_alunos, matriculas_reprovados):
    """Gera um relatório dos alunos reprovados e suas médias."""
    relatorio = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula, {})
        nome = aluno.get('nome', 'Desconhecido')
        media = aluno.get('media', 0)
        relatorio.append(f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}')
    return relatorio

def relatorio_completo(dados_alunos):
    """Gera um relatório completo com a média de todos os alunos."""
    relatorio = []
    for matricula, aluno in dados_alunos.items():
        nome = aluno['nome']
        media = aluno['media']
        status = 'Reprovado' if verificar_reprovacao(media) else 'Aprovado'
        relatorio.append(
            f'Aluno: {nome} – Matrícula: {matricula} – '
            f'1º Bimestre: {aluno["notas"][0]} – 2º Bimestre: {aluno["notas"][1]} – '
            f'3º Bimestre: {aluno["notas"][2]} – 4º Bimestre: {aluno["notas"][3]} – '
            f'Média Final: {media:.2f} – Status: {status}'
        )
    return relatorio
