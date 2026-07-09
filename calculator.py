from converter import to_decimal, from_decimal
from utils import print_result
from history import add_calculator_record
from validator import validate_base, validate_number_for_base
from representations import show_representations


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

        validate_base(base)

        number1 = input("First number: ").strip().upper()
        number2 = input("Second number: ").strip().upper()
        
        validate_number_for_base(number1, base)
        validate_number_for_base(number2, base)

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
        
        formatted_result = from_decimal(result, base)
        
        add_calculator_record(
        number1,
        number2,
        operation,
        base,
        formatted_result,
        result
        )

        print_result(
            "Calculation Result",
            f"""
        Expression:

        {number1} {operation} {number2}

        Base:

        {base}

        Answer:

        {formatted_result}

        Decimal:

        {result}
        """
        )
        
        show_representations(result)

    except ValueError:
        print("\nInvalid input.")