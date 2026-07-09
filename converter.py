from utils import print_result
from history import add_converter_record
from validator import (validate_base, validate_number, validate_number_for_base)


DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number: str, base: int) -> int:
    """
    Перевод числа из указанной системы счисления
    в десятичную.
    """

    return int(number, base)


def from_decimal(number: int, base: int) -> str:
    """
    Перевод десятичного числа
    в указанную систему счисления.
    """

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        number, remainder = divmod(number, base)
        result = DIGITS[remainder] + result

    return result


def convert_number(number: str, from_base: int, to_base: int) -> str:

    decimal = to_decimal(number, from_base)

    return from_decimal(decimal, to_base)


def converter_menu():

    print("\n========== Number Converter ==========\n")

    try:

        number = input("Number: ").upper()

        from_base = int(input("From base (2-36): "))

        to_base = int(input("To base (2-36): "))
        
        validate_base(from_base)
        validate_base(to_base)

        validate_number_for_base(number, from_base)

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

        print_result(
           "Conversion Result",
           f"""
        Number: {number}

        From base: {from_base}

        To base: {to_base}

        Answer:

        {result}
        """
        )

    except ValueError:

        print("\nInvalid number or base.")