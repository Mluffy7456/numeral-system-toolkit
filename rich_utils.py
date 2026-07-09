from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def success(message: str):
    console.print(f"[bold green]✓ {message}[/]")


def error(message: str):
    console.print(f"[bold red]✗ {message}[/]")


def warning(message: str):
    console.print(f"[bold yellow]! {message}[/]")


def info(message: str):
    console.print(f"[cyan]{message}[/]")


def title(text: str):
    console.print(
        Panel.fit(
            text,
            border_style="bright_blue"
        )
    )


def pause():
    input("\nPress Enter to continue...")