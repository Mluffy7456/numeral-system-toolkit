DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_base(base: int):

    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36.")


def validate_number(number: str):

    if not number:
        raise ValueError("Number cannot be empty.")


def validate_number_for_base(number: str, base: int):

    validate_base(base)
    validate_number(number)

    allowed = DIGITS[:base]

    for symbol in number.upper():

        if symbol not in allowed:
            raise ValueError(
                f"'{symbol}' is not valid for base {base}."
            )