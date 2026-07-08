from converter import to_decimal, from_decimal
from utils import print_result

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
    "%": lambda a, b: a % b,
}


def calculator_menu():

    print("\n========== Calculator ==========\n")

    try:

        base = int(input("Base (2-36): "))

        if not 2 <= base <= 36:
            print("\nBase must be between 2 and 36.")
            return

        number1 = input("First number: ").strip().upper()
        number2 = input("Second number: ").strip().upper()

        operation = input("Operation (+ - * / %): ").strip()

        if operation not in OPERATIONS:
            print("\nUnknown operation.")
            return

        decimal1 = to_decimal(number1, base)
        decimal2 = to_decimal(number2, base)

        if operation in ("/", "%") and decimal2 == 0:
            print("\nDivision by zero.")
            return

        result = OPERATIONS[operation](decimal1, decimal2)

        print_result(
            "Calculation Result",
            f"""
        Expression:

        {number1} {operation} {number2}

        Base:

        {base}

        Answer:

        {from_decimal(result, base)}

        Decimal:

        {result}
        """
        )

    except ValueError:
        print("\nInvalid input.")