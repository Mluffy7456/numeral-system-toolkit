from rich.prompt import Prompt

from rich_utils import console, title, success, error

from history import add_converter_record
from validator import validate_base, validate_number_for_base
from representations import show_representations
from number_utils import from_decimal

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_decimal(number: str, base: int) -> int:
    return int(number, base)


def from_decimal(number: int, base: int) -> str:

    if number == 0:
        return "0"

    negative = number < 0
    number = abs(number)

    result = ""

    while number:

        number, remainder = divmod(number, base)
        result = DIGITS[remainder] + result

    if negative:
        result = "-" + result

    return result


def convert_number(number: str,
                   from_base: int,
                   to_base: int) -> str:

    decimal = to_decimal(number, from_base)

    return from_decimal(decimal, to_base)


def converter_menu():

    title("Number Converter")

    try:

        number = Prompt.ask("Number").strip().upper()

        from_base = int(
            Prompt.ask("From base (2-36)")
        )

        to_base = int(
            Prompt.ask("To base (2-36)")
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

        success("Conversion completed successfully.")

        console.print()

        console.print(
            f"[bold cyan]Number[/]     : {number}"
        )

        console.print(
            f"[bold cyan]From Base[/]  : {from_base}"
        )

        console.print(
            f"[bold cyan]To Base[/]    : {to_base}"
        )

        console.print(
            f"[bold green]Result[/]     : {result}"
        )

        show_representations(
            to_decimal(result, to_base)
        )

    except ValueError as e:

        error(str(e))