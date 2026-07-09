from converter import to_decimal, from_decimal
from validator import validate_base, validate_number_for_base
from utils import print_result
from history import add_bitwise_record


BIT_WIDTHS = {
    "1": 8,
    "2": 16,
    "3": 32,
    "4": 64
}

def bitwise_menu():

    print("\n========== Bitwise Operations ==========\n")

    try:

        base = int(input("Base (2-36): "))
        validate_base(base)

        print("\nBit width")
        print("1. 8-bit")
        print("2. 16-bit")
        print("3. 32-bit")
        print("4. 64-bit")

        width_choice = input("\nChoose: ").strip()

        if width_choice not in BIT_WIDTHS:
            print("\nInvalid choice.")
            return

        bit_width = BIT_WIDTHS[width_choice]
        mask = (1 << bit_width) - 1

        number1 = input("\nFirst number: ").strip().upper()
        validate_number_for_base(number1, base)

        print("\nOperations")
        print("1. AND")
        print("2. OR")
        print("3. XOR")
        print("4. NAND")
        print("5. NOR")
        print("6. NOT")

        operation_choice = input("\nChoose: ").strip()

        if operation_choice not in ("1", "2", "3", "4", "5", "6"):
            print("\nUnknown operation.")
            return

        decimal1 = to_decimal(number1, base)

        if operation_choice != "6":

            number2 = input("\nSecond number: ").strip().upper()
            validate_number_for_base(number2, base)

            decimal2 = to_decimal(number2, base)

        else:

            number2 = "-"
            decimal2 = 0

        if operation_choice == "1":
            operation_name = "AND"
            result = decimal1 & decimal2

        elif operation_choice == "2":
            operation_name = "OR"
            result = decimal1 | decimal2

        elif operation_choice == "3":
            operation_name = "XOR"
            result = decimal1 ^ decimal2

        elif operation_choice == "4":
            operation_name = "NAND"
            result = ~(decimal1 & decimal2) & mask

        elif operation_choice == "5":
            operation_name = "NOR"
            result = ~(decimal1 | decimal2) & mask

        else:
            operation_name = "NOT"
            result = (~decimal1) & mask

        formatted_result = from_decimal(result, base)

        if base == 2:
            formatted_result = formatted_result.zfill(bit_width)

        add_bitwise_record(
            operation_name,
            number1,
            number2,
            base,
            formatted_result
        )

        print_result(
            "Bitwise Result",
            f"""
Operation:
{operation_name}

Bit Width:
{bit_width}

Expression:
{number1} {operation_name} {number2}

Result ({base}):
{formatted_result}

Binary:
{from_decimal(result, 2).zfill(bit_width)}

Octal:
{from_decimal(result, 8)}

Decimal:
{result}

Hexadecimal:
{from_decimal(result, 16)}
"""
        )

    except ValueError as e:
        print(f"\n{e}")