from rich.prompt import Prompt

from converter import to_decimal, from_decimal
from history import add_calculator_record
from validator import validate_base, validate_number_for_base
from representations import show_representations
from rich_utils import console, title, success, error


OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "%": lambda a, b: a % b,
}


def calculator_menu():

    title("Calculator")

    try:

        base = int(
            Prompt.ask("Base (2-36)")
        )

        validate_base(base)

        number1 = Prompt.ask(
            "First number"
        ).strip().upper()

        number2 = Prompt.ask(
            "Second number"
        ).strip().upper()

        validate_number_for_base(number1, base)
        validate_number_for_base(number2, base)

        operation = Prompt.ask(
            "Operation (+ - * / %)"
        ).strip()

        if operation not in OPERATIONS:
            error("Unknown operation.")
            return

        decimal1 = to_decimal(number1, base)
        decimal2 = to_decimal(number2, base)

        if operation in ("/", "%") and decimal2 == 0:
            error("Division by zero.")
            return

        result = OPERATIONS[operation](
            decimal1,
            decimal2
        )

        formatted_result = from_decimal(
            result,
            base
        )

        add_calculator_record(
            number1,
            number2,
            operation,
            base,
            formatted_result,
            result
        )

        success("Calculation completed successfully.")

        console.print()

        console.print(
            f"[bold cyan]Expression[/] : {number1} {operation} {number2}"
        )

        console.print(
            f"[bold cyan]Base[/]       : {base}"
        )

        console.print(
            f"[bold green]Result[/]     : {formatted_result}"
        )

        console.print(
            f"[bold yellow]Decimal[/]   : {result}"
        )

        show_representations(result)

    except ValueError as e:

        error(str(e))