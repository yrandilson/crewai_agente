"""
main.py — Ponto de entrada da aplicação
Executa o CrewAI com interface CLI usando Rich.
"""

import sys
import time
import argparse
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich import box

console = Console()


def banner():
    console.print(
        Panel.fit(
            "[bold cyan]🤖  CrewAI — Agente de Pesquisa e Análise[/bold cyan]\n"
            "[dim]Pipeline: Pesquisador → Analista → Redator → Gerente[/dim]",
            border_style="cyan",
            padding=(1, 4),
        )
    )


def exibir_agentes():
    table = Table(title="👥 Agentes do Sistema", box=box.ROUNDED, border_style="dim cyan")
    table.add_column("Agente",      style="bold yellow", width=22)
    table.add_column("Papel",       style="white",       width=28)
    table.add_column("Ferramentas", style="green",       width=30)

    table.add_row(
        "🔍 Pesquisador",
        "Pesquisa na internet",
        "busca_web, data_hora",
    )
    table.add_row(
        "📊 Analista",
        "Análise crítica dos dados",
        "analisar_texto, data_hora",
    )
    table.add_row(
        "✍️  Redator",
        "Produz o relatório final",
        "salvar_arquivo, data_hora",
    )
    table.add_row(
        "🎯 Gerente",
        "Revisão e aprovação",
        "salvar_arquivo, data_hora",
    )
    console.print(table)
    console.print()


def solicitar_tema() -> str:
    console.print("[bold]📌 Informe o tema para análise:[/bold]")
    tema = console.input("[cyan]➜  [/cyan]").strip()
    if not tema:
        console.print("[red]Tema não pode estar vazio![/red]")
        sys.exit(1)
    return tema


def exibir_resultado(resultado: str, tema: str):
    console.rule("[bold green]✅ Execução Concluída[/bold green]")
    console.print()

    # Tenta exibir o relatório salvo
    caminho = Path("output/relatorio_revisado.md")
    if not caminho.exists():
        caminho = Path("output/relatorio_final.md")

    if caminho.exists():
        console.print(
            Panel(
                f"[green]Relatório salvo em:[/green] [bold]{caminho}[/bold]",
                border_style="green",
            )
        )
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
        console.print(Markdown(conteudo))
    else:
        console.print(
            Panel(resultado, title="[bold]Resultado[/bold]", border_style="green")
        )


def main():
    parser = argparse.ArgumentParser(
        description="CrewAI — Agente de Pesquisa e Análise"
    )
    parser.add_argument(
        "--tema", "-t",
        type=str,
        help="Tema para pesquisa e análise",
        default=None,
    )
    parser.add_argument(
        "--listar-agentes", "-l",
        action="store_true",
        help="Lista os agentes disponíveis e sai",
    )
    args = parser.parse_args()

    banner()

    if args.listar_agentes:
        exibir_agentes()
        return

    exibir_agentes()

    # Obtém o tema
    tema = args.tema or solicitar_tema()

    console.print(
        Panel(
            f"[bold]Tema:[/bold] [yellow]{tema}[/yellow]",
            border_style="yellow",
            title="🚀 Iniciando pipeline",
        )
    )
    console.print()

    # Importa aqui para não bloquear o --help
    from crew import executar

    inicio = time.time()

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task(
                "[cyan]Executando agentes... (isso pode levar alguns minutos)[/cyan]",
                total=None,
            )
            resultado = executar(tema)

        duracao = time.time() - inicio
        console.print(
            f"\n[dim]⏱  Tempo total: {duracao:.1f}s[/dim]\n"
        )
        exibir_resultado(str(resultado), tema)

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠  Execução interrompida pelo usuário.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ Erro durante a execução:[/red] {e}")
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
