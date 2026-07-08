from utils import print_result


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
        
        if not number:
           print("\nNumber cannot be empty.")
           return

        from_base = int(input("From base (2-36): "))

        to_base = int(input("To base (2-36): "))
        
        if not 2 <= from_base <= 36:
           print("\nSource base must be between 2 and 36.")
           return

        if not 2 <= to_base <= 36:
           print("\nTarget base must be between 2 and 36.")
           return

        result = convert_number(
            number,
            from_base,
            to_base
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