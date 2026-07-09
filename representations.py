from rich.table import Table
from rich import box

from converter import from_decimal
from rich_utils import console


def group_bits(binary: str, group: int = 4) -> str:
    """
    Groups binary digits for better readability.

    Example:
    10101010 -> 1010 1010
    """

    padding = (-len(binary)) % group
    binary = "0" * padding + binary

    return " ".join(
        binary[i:i + group]
        for i in range(0, len(binary), group)
    )


def show_representations(number: int, bit_width: int | None = None):

    binary = from_decimal(number, 2)

    if bit_width:
        binary = binary.zfill(bit_width)

    binary = group_bits(binary)

    table = Table(
        title="Representations",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("System", style="green")
    table.add_column("Value", style="yellow")

    table.add_row("Binary", binary)
    table.add_row("Octal", from_decimal(number, 8))
    table.add_row("Decimal", str(number))
    table.add_row("Hexadecimal", from_decimal(number, 16))

    console.print()
    console.print(table)