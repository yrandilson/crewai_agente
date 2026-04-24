"""
tasks/tarefas.py — Definição de todas as tarefas do pipeline
"""

from crewai import Task
from crewai import Agent


def criar_tarefa_pesquisa(agente: Agent, tema: str) -> Task:
    return Task(
        description=(
            f"Pesquise extensivamente sobre o tema: **{tema}**.\n\n"
            "Suas responsabilidades:\n"
            "1. Realize pelo menos 3 buscas diferentes sobre o tema\n"
            "2. Colete informações de fontes variadas\n"
            "3. Registre a data/hora da pesquisa\n"
            "4. Organize os dados em tópicos: contexto, situação atual, "
            "   dados relevantes, tendências e referências\n\n"
            "Entregável: Um documento estruturado com todas as informações "
            "coletadas, organizadas por subtema."
        ),
        expected_output=(
            "Documento de pesquisa com no mínimo 500 palavras contendo:\n"
            "- Contexto e definição do tema\n"
            "- Situação atual (dados e fatos)\n"
            "- Tendências identificadas\n"
            "- Fontes consultadas\n"
            "- Data/hora da pesquisa"
        ),
        agent=agente,
    )


def criar_tarefa_analise(agente: Agent, tema: str) -> Task:
    return Task(
        description=(
            f"Com base na pesquisa realizada sobre '{tema}', faça uma "
            "análise crítica e profunda do conteúdo.\n\n"
            "Suas responsabilidades:\n"
            "1. Analise as estatísticas do texto de pesquisa\n"
            "2. Identifique os 5 principais insights\n"
            "3. Mapeie oportunidades e riscos relacionados ao tema\n"
            "4. Identifique gaps de informação (o que ainda é incerto)\n"
            "5. Faça uma avaliação de relevância de cada ponto\n\n"
            "Use a ferramenta 'analisar_texto' para obter métricas quantitativas."
        ),
        expected_output=(
            "Relatório analítico contendo:\n"
            "- Métricas do texto (palavras, sentenças, termos-chave)\n"
            "- Top 5 insights identificados\n"
            "- Matriz de oportunidades e riscos\n"
            "- Lacunas de conhecimento\n"
            "- Score de relevância por subtema (1-10)"
        ),
        agent=agente,
    )


def criar_tarefa_redacao(agente: Agent, tema: str) -> Task:
    return Task(
        description=(
            f"Produza um relatório executivo completo sobre '{tema}' "
            "combinando a pesquisa e a análise realizadas.\n\n"
            "O relatório deve seguir esta estrutura:\n"
            "# Relatório Executivo: {tema}\n"
            "## 1. Sumário Executivo (3-5 parágrafos)\n"
            "## 2. Contexto e Cenário Atual\n"
            "## 3. Principais Descobertas\n"
            "## 4. Análise de Oportunidades e Riscos\n"
            "## 5. Tendências e Perspectivas\n"
            "## 6. Recomendações Estratégicas\n"
            "## 7. Conclusão\n"
            "## 8. Fontes e Referências\n\n"
            "Após finalizar, use a ferramenta 'salvar_arquivo' para salvar "
            "o relatório com o nome 'relatorio_final.md'."
        ),
        expected_output=(
            "Relatório executivo completo em Markdown com:\n"
            "- Mínimo de 800 palavras\n"
            "- Todas as 8 seções preenchidas\n"
            "- Linguagem profissional e clara\n"
            "- Arquivo salvo em output/relatorio_final.md"
        ),
        agent=agente,
    )


def criar_tarefa_revisao(agente: Agent, tema: str) -> Task:
    return Task(
        description=(
            f"Revise e aprove o relatório executivo sobre '{tema}'.\n\n"
            "Checklist de revisão:\n"
            "□ O relatório está completo (todas as seções)?\n"
            "□ As informações são consistentes entre as seções?\n"
            "□ O sumário executivo reflete o conteúdo completo?\n"
            "□ As recomendações são baseadas em evidências do relatório?\n"
            "□ A linguagem está clara e profissional?\n"
            "□ As fontes estão citadas corretamente?\n\n"
            "Após a revisão:\n"
            "- Se aprovado: adicione uma seção '## ✅ Aprovação' ao final\n"
            "- Se necessitar ajustes: liste as correções necessárias\n"
            "- Salve a versão final revisada como 'relatorio_revisado.md'"
        ),
        expected_output=(
            "Relatório revisado e aprovado com:\n"
            "- Checklist de qualidade preenchido\n"
            "- Seção de aprovação com assinatura do gerente\n"
            "- Eventuais correções aplicadas\n"
            "- Arquivo final salvo em output/relatorio_revisado.md"
        ),
        agent=agente,
    )
