# 🤖 CrewAI — Agente de Pesquisa e Análise

Pipeline multi-agente completo usando [CrewAI](https://crewai.com).
Pesquisa, analisa e gera relatórios executivos sobre qualquer tema.

---

## 🏗️ Arquitetura

```
crewai_agente/
├── main.py              # CLI principal (Rich)
├── crew.py              # Orquestração do Crew
├── config.py            # Configurações e variáveis de ambiente
├── requirements.txt
├── .env.example
├── agents/
│   └── agentes.py       # 4 agentes especializados
├── tasks/
│   └── tarefas.py       # 4 tarefas encadeadas
├── tools/
│   └── custom_tools.py  # 4 ferramentas customizadas
└── output/              # Relatórios gerados aqui
```

## 👥 Agentes

| Agente         | Papel                        | Ferramentas                  |
|----------------|------------------------------|------------------------------|
| 🔍 Pesquisador | Pesquisa na internet         | busca_web, data_hora         |
| 📊 Analista    | Análise crítica dos dados    | analisar_texto, data_hora    |
| ✍️ Redator     | Produz o relatório final     | salvar_arquivo, data_hora    |
| 🎯 Gerente     | Revisão e aprovação          | salvar_arquivo, data_hora    |

## 🔧 Ferramentas Customizadas

- **busca_web** — Busca no DuckDuckGo (sem API key necessária)
- **analisar_texto** — Métricas de texto: palavras, sentenças, top termos
- **salvar_arquivo** — Persiste resultados em `output/`
- **data_hora_atual** — Timestamp atual

## 🚀 Instalação

```bash
# 1. Clone / extraia o projeto
cd crewai_agente

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate.bat     # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure suas chaves
cp .env.example .env
# Edite o .env e coloque sua OPENAI_API_KEY
```

## ▶️ Uso

```bash
# Modo interativo (pergunta o tema)
python main.py

# Passando o tema direto
python main.py --tema "Inteligência Artificial no Brasil em 2025"

# Listar agentes
python main.py --listar-agentes

# Atalho
python main.py -t "mercado de SaaS para pequenas empresas"
```

## 📄 Output

Os relatórios são salvos automaticamente em `output/`:
- `relatorio_final.md` — Relatório do Redator
- `relatorio_revisado.md` — Relatório revisado e aprovado pelo Gerente

## ⚙️ Configuração

Edite o arquivo `.env`:

```env
OPENAI_API_KEY=sk-...         # Obrigatório
OPENAI_MODEL_NAME=gpt-4o      # Padrão: gpt-4o (pode usar gpt-3.5-turbo)
VERBOSE=true                  # Mostra raciocínio dos agentes
```

## 🔄 Fluxo do Pipeline

```
[Usuário fornece tema]
        ↓
  🔍 Pesquisador
  └── Busca 3+ fontes sobre o tema
  └── Output: documento de pesquisa estruturado
        ↓
  📊 Analista  (recebe output do Pesquisador)
  └── Analisa métricas e conteúdo
  └── Output: 5 insights + oportunidades/riscos
        ↓
  ✍️ Redator  (recebe outputs do Pesquisador + Analista)
  └── Produz relatório executivo em 8 seções
  └── Salva em output/relatorio_final.md
        ↓
  🎯 Gerente  (recebe output do Redator)
  └── Aplica checklist de qualidade
  └── Aprova ou solicita correções
  └── Salva em output/relatorio_revisado.md
```

## 💡 Exemplos de Temas

```bash
python main.py -t "mercado de fintechs no Nordeste"
python main.py -t "automação industrial com IA"
python main.py -t "barbearias e salões de beleza no Brasil"
python main.py -t "SaaS para pequenas empresas 2025"
python main.py -t "agro tech no Ceará"
```

## 📦 Dependências Principais

- `crewai` — Framework multi-agente
- `langchain-openai` — Integração com GPT-4o
- `duckduckgo-search` — Busca web sem API key
- `rich` — Interface CLI colorida
- `python-dotenv` — Variáveis de ambiente
