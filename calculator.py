from rich.prompt import Prompt

from number_utils import from_decimal
from converter import to_decimal

from history import add_calculator_record
from validator import validate_base, validate_number_for_base
from representations import show_representations

from rich_utils import (
    console,
    title,
    success,
    error
)

from language import t


OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "%": lambda a, b: a % b,
}


def calculator_menu():

    title(t("calculator.title"))

    try:

        base = int(
            Prompt.ask(
                t("calculator.base")
            )
        )

        validate_base(base)

        number1 = Prompt.ask(
            t("calculator.first_number")
        ).strip().upper()

        number2 = Prompt.ask(
            t("calculator.second_number")
        ).strip().upper()

        validate_number_for_base(number1, base)
        validate_number_for_base(number2, base)

        operation = Prompt.ask(
            t("calculator.operation")
        ).strip()

        if operation not in OPERATIONS:
            error("error.unknown_operation")
            return

        decimal1 = to_decimal(number1, base)
        decimal2 = to_decimal(number2, base)

        if operation in ("/", "%") and decimal2 == 0:
            error("error.division_zero")
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

        success("calculator.success")

        console.print()

        console.print(
            f"[bold cyan]{t('calculator.expression')}[/] : {number1} {operation} {number2}"
        )

        console.print(
            f"[bold cyan]{t('calculator.base')}[/]       : {base}"
        )

        console.print(
            f"[bold green]{t('calculator.result')}[/]     : {formatted_result}"
        )

        console.print(
            f"[bold yellow]{t('calculator.decimal')}[/]   : {result}"
        )

        show_representations(result)

    except ValueError as e:

        error(str(e))