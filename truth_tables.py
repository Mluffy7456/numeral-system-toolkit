from itertools import product
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t

OPERATIONS = {
    "1": ("AND", lambda a, b: a and b),
    "2": ("OR", lambda a, b: a or b),
    "3": ("XOR", lambda a, b: a ^ b),
    "4": ("NAND", lambda a, b: not (a and b)),
    "5": ("NOR", lambda a, b: not (a or b)),
    "6": ("XNOR", lambda a, b: not (a ^ b)),
}

def truth_table_menu():
    title(t("truth.title"))
    console.print(f"[cyan]1.[/] AND\n[cyan]2.[/] OR\n[cyan]3.[/] XOR\n[cyan]4.[/] NAND\n[cyan]5.[/] NOR\n[cyan]6.[/] XNOR\n[cyan]0.[/] Back")
    choice = Prompt.ask(t("choose")).strip()
    if choice == "0":
        return
    if choice not in OPERATIONS:
        error(t("error.unknown_operation"))
        return
    name, fn = OPERATIONS[choice]
    table = Table(title=f"{name} {t('truth.table')}", box=box.ROUNDED, header_style="bold cyan")
    table.add_column("A", justify="center")
    table.add_column("B", justify="center")
    table.add_column("Result", justify="center")
    for a, b in product((0, 1), repeat=2):
        table.add_row(str(a), str(b), str(int(fn(a, b))))
    console.print(table)
