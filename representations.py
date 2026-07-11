from rich.table import Table
from rich import box

from number_utils import from_decimal
from rich_utils import console
from language import t


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


def show_representations(
    number: int,
    bit_width: int | None = None
):

    binary = from_decimal(number, 2)

    if bit_width:
        binary = binary.zfill(bit_width)

    binary = group_bits(binary)

    table = Table(
        title=t("representations.title"),
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column(
        t("representations.system"),
        style="green"
    )

    table.add_column(
        t("representations.value"),
        style="yellow"
    )

    table.add_row(
        t("representations.binary"),
        binary
    )

    table.add_row(
        t("representations.octal"),
        from_decimal(number, 8)
    )

    table.add_row(
        t("representations.decimal"),
        str(number)
    )

    table.add_row(
        t("representations.hexadecimal"),
        from_decimal(number, 16)
    )

    console.print()
    console.print(table)