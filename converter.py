from rich.prompt import Prompt

from rich_utils import console, title, success, error

from language import t

from history import add_converter_record
from validator import validate_base, validate_number_for_base
from representations import show_representations
from number_utils import from_decimal


def to_decimal(number: str, base: int) -> int:
    return int(number, base)


def convert_number(
    number: str,
    from_base: int,
    to_base: int
) -> str:

    decimal = to_decimal(number, from_base)

    return from_decimal(decimal, to_base)


def converter_menu():

    title(t("converter.title"))

    try:

        number = Prompt.ask(
            t("converter.number")
        ).strip().upper()

        from_base = int(
            Prompt.ask(
                t("converter.from_base")
            )
        )

        to_base = int(
            Prompt.ask(
                t("converter.to_base")
            )
        )

        validate_base(from_base)
        validate_base(to_base)

        validate_number_for_base(
            number,
            from_base
        )

        result = convert_number(
            number,
            from_base,
            to_base
        )

        add_converter_record(
            number,
            from_base,
            to_base,
            result
        )

        success("converter.success")

        console.print()

        console.print(
            f"[bold cyan]{t('converter.number')}[/]      : {number}"
        )

        console.print(
            f"[bold cyan]{t('converter.from_base')}[/]   : {from_base}"
        )

        console.print(
            f"[bold cyan]{t('converter.to_base')}[/]     : {to_base}"
        )

        console.print(
            f"[bold green]{t('converter.result')}[/]      : {result}"
        )

        show_representations(
            to_decimal(result, to_base)
        )

    except ValueError as e:

        error(str(e))