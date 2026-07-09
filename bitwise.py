from rich.prompt import Prompt
from number_utils import from_decimal
from converter import to_decimal
from validator import validate_base, validate_number_for_base
from history import add_bitwise_record
from representations import show_representations
from rich_utils import console, title, success, error


BIT_WIDTHS = {
    "1": 8,
    "2": 16,
    "3": 32,
    "4": 64
}


def and_operation(a, b, mask):
    return a & b


def or_operation(a, b, mask):
    return a | b


def xor_operation(a, b, mask):
    return a ^ b


def nand_operation(a, b, mask):
    return ~(a & b) & mask


def nor_operation(a, b, mask):
    return ~(a | b) & mask


def not_operation(a, b, mask):
    return ~a & mask


def shift_left(a, shift, mask):
    return (a << shift) & mask


def shift_right(a, shift, mask):
    return a >> shift


def rotate_left(a, shift, width):

    shift %= width
    mask = (1 << width) - 1

    return (
        ((a << shift) |
         (a >> (width - shift)))
        & mask
    )


def rotate_right(a, shift, width):

    shift %= width
    mask = (1 << width) - 1

    return (
        ((a >> shift) |
         (a << (width - shift)))
        & mask
    )


OPERATIONS = {
    "1": ("AND", and_operation),
    "2": ("OR", or_operation),
    "3": ("XOR", xor_operation),
    "4": ("NAND", nand_operation),
    "5": ("NOR", nor_operation),
    "6": ("NOT", not_operation),
    "7": ("SHIFT LEFT", shift_left),
    "8": ("SHIFT RIGHT", shift_right),
    "9": ("ROTATE LEFT", rotate_left),
    "10": ("ROTATE RIGHT", rotate_right),
}

def bitwise_menu():

    title("Bitwise Operations")

    try:

        base = int(
            Prompt.ask("Base (2-36)")
        )

        validate_base(base)

        console.print()
        console.print("[bold cyan]Bit Width[/]")
        console.print("[cyan]1.[/] 8-bit")
        console.print("[cyan]2.[/] 16-bit")
        console.print("[cyan]3.[/] 32-bit")
        console.print("[cyan]4.[/] 64-bit")

        width_choice = Prompt.ask("Choose")

        if width_choice not in BIT_WIDTHS:
            error("Invalid bit width.")
            return

        bit_width = BIT_WIDTHS[width_choice]
        mask = (1 << bit_width) - 1

        console.print()

        number1 = Prompt.ask(
            "First number"
        ).strip().upper()

        validate_number_for_base(number1, base)

        console.print()
        console.print("[bold cyan]Operations[/]")
        console.print("[cyan]1.[/] AND")
        console.print("[cyan]2.[/] OR")
        console.print("[cyan]3.[/] XOR")
        console.print("[cyan]4.[/] NAND")
        console.print("[cyan]5.[/] NOR")
        console.print("[cyan]6.[/] NOT")
        console.print("[cyan]7.[/] SHIFT LEFT")
        console.print("[cyan]8.[/] SHIFT RIGHT")
        console.print("[cyan]9.[/] ROTATE LEFT")
        console.print("[cyan]10.[/] ROTATE RIGHT")

        operation_choice = Prompt.ask("Choose")

        if operation_choice not in OPERATIONS:
            error("Unknown operation.")
            return

        operation_name, operation = OPERATIONS[operation_choice]

        decimal1 = to_decimal(number1, base)

        decimal2 = 0
        number2 = "-"

        shift = 0

        if operation_choice in (
            "1",
            "2",
            "3",
            "4",
            "5"
        ):

            number2 = Prompt.ask(
                "Second number"
            ).strip().upper()

            validate_number_for_base(
                number2,
                base
            )

            decimal2 = to_decimal(
                number2,
                base
            )

        elif operation_choice in (
            "7",
            "8",
            "9",
            "10"
        ):

            shift = int(
                Prompt.ask("Shift amount")
            )

        if operation_choice == "6":

            result = operation(
                decimal1,
                decimal2,
                mask
            )

        elif operation_choice in (
            "7",
            "8"
        ):

            result = operation(
                decimal1,
                shift,
                mask
            )

        elif operation_choice == "9":

            result = rotate_left(
                decimal1,
                shift,
                bit_width
            )

        elif operation_choice == "10":

            result = rotate_right(
                decimal1,
                shift,
                bit_width
            )

        else:

            result = operation(
                decimal1,
                decimal2,
                mask
            )

        formatted_result = from_decimal(
            result,
            base
        )

        if base == 2:

            formatted_result = formatted_result.zfill(
                bit_width
            )

        add_bitwise_record(
            operation_name,
            number1,
            number2,
            base,
            formatted_result,
            shift if operation_choice in ("7", "8", "9", "10") else None
        )

        success("Operation completed successfully.")

        console.print()

        console.print(
            f"[bold cyan]Operation[/] : {operation_name}"
        )

        console.print(
            f"[bold cyan]Bit Width[/] : {bit_width}"
        )

        if operation_choice in (
            "7",
            "8",
            "9",
            "10"
        ):

            console.print(
                f"[bold cyan]Shift[/]     : {shift}"
            )

        if operation_choice == "6":

            console.print(
                f"[bold cyan]Expression[/] : {operation_name} {number1}"
            )

        elif operation_choice in (
            "7",
            "8",
            "9",
            "10"
        ):

            console.print(
                f"[bold cyan]Expression[/] : {number1} ({shift})"
            )

        else:

            console.print(
                f"[bold cyan]Expression[/] : {number1} {operation_name} {number2}"
            )

        console.print(
            f"[bold green]Result[/]    : {formatted_result}"
        )

        show_representations(
            result,
            bit_width
        )

    except ValueError as e:

        error(str(e))