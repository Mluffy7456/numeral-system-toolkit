from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t
from converter import to_decimal
from validator import validate_base, validate_number_for_base

def bit_representation_menu():
    title(t("bitrep.title"))
    try:
        number = Prompt.ask(t("bitrep.number")).strip().upper()
        base = int(Prompt.ask(t("bitrep.base")))
        width = int(Prompt.ask(t("bitrep.width")))
        validate_base(base)
        validate_number_for_base(number, base)
        if width <= 0 or width > 1024:
            raise ValueError(t("error.invalid_width"))
        value = to_decimal(number, base)
        if value < 0:
            raise ValueError(t("error.negative_not_supported"))
        minimum = 1 if value == 0 else value.bit_length()
        if minimum > width:
            raise ValueError(t("error.value_too_large").format(width=width))
        bits = format(value, f"0{width}b")
        table = Table(title=t("bitrep.table"), box=box.ROUNDED, header_style="bold cyan")
        table.add_column(t("bitrep.index"), justify="center")
        table.add_column(t("bitrep.bit"), justify="center")
        for i, bit in enumerate(bits):
            table.add_row(str(width - i - 1), bit)
        console.print(table)
        console.print(f"[bold green]{t('bitrep.binary')}[/]: {bits}")
    except ValueError as e:
        error(str(e))
