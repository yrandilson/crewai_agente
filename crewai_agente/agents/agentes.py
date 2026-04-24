"""
agents/agentes.py — Definição de todos os agentes do sistema
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL, VERBOSE
from tools import busca_web_tool, analisar_texto_tool, salvar_arquivo_tool, data_hora_tool


def get_llm():
    return ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.3,
    )


# ══════════════════════════════════════════════
# AGENTE 1 — Pesquisador
# ══════════════════════════════════════════════
def criar_agente_pesquisador() -> Agent:
    return Agent(
        role="Pesquisador Especialista",
        goal=(
            "Coletar informações precisas, atualizadas e relevantes "
            "sobre o tema solicitado usando buscas na internet."
        ),
        backstory=(
            "Você é um pesquisador experiente com habilidade de encontrar "
            "informações confiáveis em diversas fontes. Você sabe filtrar "
            "o que é relevante e sintetizar dados de múltiplas fontes "
            "em um resumo coeso e factual."
        ),
        tools=[busca_web_tool, data_hora_tool],
        llm=get_llm(),
        verbose=VERBOSE,
        allow_delegation=False,
        max_iter=5,
    )


# ══════════════════════════════════════════════
# AGENTE 2 — Analista
# ══════════════════════════════════════════════
def criar_agente_analista() -> Agent:
    return Agent(
        role="Analista de Dados e Conteúdo",
        goal=(
            "Analisar profundamente as informações coletadas, "
            "identificar padrões, tendências e insights relevantes."
        ),
        backstory=(
            "Você é um analista sênior com expertise em transformar dados "
            "brutos em insights acionáveis. Você possui pensamento crítico "
            "aguçado e sabe identificar o que realmente importa em um "
            "conjunto de informações, separando fatos de opiniões."
        ),
        tools=[analisar_texto_tool, data_hora_tool],
        llm=get_llm(),
        verbose=VERBOSE,
        allow_delegation=False,
        max_iter=5,
    )


# ══════════════════════════════════════════════
# AGENTE 3 — Redator/Escritor
# ══════════════════════════════════════════════
def criar_agente_redator() -> Agent:
    return Agent(
        role="Redator Técnico Sênior",
        goal=(
            "Produzir relatórios claros, bem estruturados e profissionais "
            "com base nas pesquisas e análises fornecidas."
        ),
        backstory=(
            "Você é um redator técnico com anos de experiência em produzir "
            "documentos executivos, relatórios de mercado e artigos técnicos. "
            "Seu estilo é claro, objetivo e direto ao ponto, sempre com "
            "estrutura lógica e linguagem acessível ao público-alvo."
        ),
        tools=[salvar_arquivo_tool, data_hora_tool],
        llm=get_llm(),
        verbose=VERBOSE,
        allow_delegation=False,
        max_iter=5,
    )


# ══════════════════════════════════════════════
# AGENTE 4 — Gerente / Coordenador
# ══════════════════════════════════════════════
def criar_agente_gerente() -> Agent:
    return Agent(
        role="Gerente de Projeto e Qualidade",
        goal=(
            "Coordenar o trabalho dos agentes, garantir a qualidade "
            "do output final e aprovar o relatório antes da entrega."
        ),
        backstory=(
            "Você é um gerente de projetos experiente com senso crítico "
            "apurado. Você revisa o trabalho da equipe, aponta melhorias, "
            "garante consistência e aprova apenas o que atende ao padrão "
            "de qualidade exigido pelo cliente."
        ),
        tools=[salvar_arquivo_tool, data_hora_tool],
        llm=get_llm(),
        verbose=VERBOSE,
        allow_delegation=True,  # Gerente pode delegar
        max_iter=5,
    )
