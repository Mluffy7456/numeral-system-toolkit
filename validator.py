from language import t

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_base(base: int):

    if not 2 <= base <= 36:
        raise ValueError(
            t("error.invalid_base")
        )


def validate_number(number: str):

    if not number:
        raise ValueError(
            t("error.empty_number")
        )


def validate_number_for_base(
    number: str,
    base: int
):

    validate_base(base)
    validate_number(number)

    allowed = DIGITS[:base]

    if number.startswith("-"):
        number = number[1:]

    if not number:

        raise ValueError(
            t("error.only_minus")
        )

    for symbol in number.upper():

        if symbol not in allowed:

            raise ValueError(

                t("error.invalid_symbol").format(
                    symbol=symbol,
                    base=base
                )

            )