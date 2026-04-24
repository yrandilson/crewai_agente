"""
tools/custom_tools.py — Ferramentas customizadas para os agentes
"""

import json
import datetime
import requests
from crewai_tools import BaseTool
from duckduckgo_search import DDGS


# ──────────────────────────────────────────────
# 1. Ferramenta de busca na web (DuckDuckGo)
# ──────────────────────────────────────────────
class BuscaWebTool(BaseTool):
    name: str = "busca_web"
    description: str = (
        "Realiza buscas na internet usando DuckDuckGo. "
        "Use para pesquisar informações atuais sobre qualquer tema. "
        "Entrada: string com os termos de busca."
    )

    def _run(self, query: str) -> str:
        try:
            with DDGS() as ddgs:
                resultados = list(ddgs.text(query, max_results=5))
            if not resultados:
                return "Nenhum resultado encontrado."
            saida = []
            for i, r in enumerate(resultados, 1):
                saida.append(
                    f"[{i}] {r.get('title', 'Sem título')}\n"
                    f"URL: {r.get('href', '')}\n"
                    f"Resumo: {r.get('body', '')}\n"
                )
            return "\n".join(saida)
        except Exception as e:
            return f"Erro ao buscar: {str(e)}"


# ──────────────────────────────────────────────
# 2. Ferramenta de análise de texto
# ──────────────────────────────────────────────
class AnalisadorTextoTool(BaseTool):
    name: str = "analisar_texto"
    description: str = (
        "Analisa estatísticas de um texto: contagem de palavras, "
        "sentenças, parágrafos e palavras mais frequentes. "
        "Entrada: o texto a ser analisado."
    )

    def _run(self, texto: str) -> str:
        palavras   = texto.split()
        sentencas  = texto.count(".") + texto.count("!") + texto.count("?")
        paragrafos = [p for p in texto.split("\n\n") if p.strip()]

        # Frequência das palavras (ignora stopwords simples)
        stopwords_pt = {
            "de", "a", "o", "que", "e", "do", "da", "em", "um", "para",
            "é", "com", "uma", "os", "no", "se", "na", "por", "mais",
            "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem",
            "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos",
            "já", "está", "eu", "também", "só", "pelo", "pela", "até",
            "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos",
        }
        freq: dict = {}
        for w in palavras:
            w_clean = w.lower().strip(".,!?;:\"'()[]")
            if w_clean and w_clean not in stopwords_pt and len(w_clean) > 2:
                freq[w_clean] = freq.get(w_clean, 0) + 1

        top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

        resultado = {
            "total_palavras":   len(palavras),
            "total_sentencas":  sentencas,
            "total_paragrafos": len(paragrafos),
            "top10_palavras":   top10,
        }
        return json.dumps(resultado, ensure_ascii=False, indent=2)


# ──────────────────────────────────────────────
# 3. Ferramenta de salvar arquivo
# ──────────────────────────────────────────────
class SalvarArquivoTool(BaseTool):
    name: str = "salvar_arquivo"
    description: str = (
        "Salva conteúdo em um arquivo de texto na pasta output/. "
        "Entrada: JSON com 'nome_arquivo' e 'conteudo'. "
        "Exemplo: {\"nome_arquivo\": \"relatorio.md\", \"conteudo\": \"# Relatório...\"}"
    )

    def _run(self, entrada: str) -> str:
        try:
            dados = json.loads(entrada)
            nome     = dados.get("nome_arquivo", "saida.txt")
            conteudo = dados.get("conteudo", "")
            caminho  = f"output/{nome}"
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(conteudo)
            return f"✅ Arquivo salvo em: {caminho}"
        except json.JSONDecodeError:
            # Tenta salvar diretamente como texto se não for JSON
            caminho = "output/saida.txt"
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(entrada)
            return f"✅ Arquivo salvo em: {caminho}"
        except Exception as e:
            return f"Erro ao salvar: {str(e)}"


# ──────────────────────────────────────────────
# 4. Ferramenta de data/hora atual
# ──────────────────────────────────────────────
class DataHoraTool(BaseTool):
    name: str = "data_hora_atual"
    description: str = (
        "Retorna a data e hora atual do sistema. "
        "Útil para registrar timestamps em relatórios."
    )

    def _run(self, _: str = "") -> str:
        agora = datetime.datetime.now()
        return agora.strftime("Data: %d/%m/%Y | Hora: %H:%M:%S")


# ──────────────────────────────────────────────
# Exporta instâncias prontas para uso
# ──────────────────────────────────────────────
busca_web_tool      = BuscaWebTool()
analisar_texto_tool = AnalisadorTextoTool()
salvar_arquivo_tool = SalvarArquivoTool()
data_hora_tool      = DataHoraTool()
