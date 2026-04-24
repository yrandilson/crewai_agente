"""
crew.py — Orquestração principal do CrewAI
Define o Crew completo e executa o pipeline de agentes.
"""

from crewai import Crew, Process
from agents import (
    criar_agente_pesquisador,
    criar_agente_analista,
    criar_agente_redator,
    criar_agente_gerente,
)
from tasks import (
    criar_tarefa_pesquisa,
    criar_tarefa_analise,
    criar_tarefa_redacao,
    criar_tarefa_revisao,
)
from config import VERBOSE


def criar_crew(tema: str) -> Crew:
    """
    Monta e retorna o Crew completo para análise de um tema.

    Pipeline:
        Pesquisador → Analista → Redator → Gerente (revisão)
    """

    # ── Agentes ──────────────────────────────────────────────────────
    pesquisador = criar_agente_pesquisador()
    analista    = criar_agente_analista()
    redator     = criar_agente_redator()
    gerente     = criar_agente_gerente()

    # ── Tarefas (ordem importa no processo sequencial) ───────────────
    t_pesquisa = criar_tarefa_pesquisa(pesquisador, tema)
    t_analise  = criar_tarefa_analise(analista, tema)
    t_redacao  = criar_tarefa_redacao(redator, tema)
    t_revisao  = criar_tarefa_revisao(gerente, tema)

    # Encadeamento: cada tarefa recebe o output da anterior como contexto
    t_analise.context  = [t_pesquisa]
    t_redacao.context  = [t_pesquisa, t_analise]
    t_revisao.context  = [t_redacao]

    # ── Crew ─────────────────────────────────────────────────────────
    crew = Crew(
        agents=[pesquisador, analista, redator, gerente],
        tasks=[t_pesquisa, t_analise, t_redacao, t_revisao],
        process=Process.sequential,   # Execução em ordem
        verbose=VERBOSE,
        memory=True,                  # Habilita memória entre tarefas
        embedder={
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"},
        },
    )

    return crew


def executar(tema: str) -> str:
    """Cria e executa o crew para o tema fornecido."""
    crew   = criar_crew(tema)
    result = crew.kickoff()
    return result
