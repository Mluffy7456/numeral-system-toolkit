DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def from_decimal(number: int, base: int) -> str:

    if number == 0:
        return "0"

    negative = number < 0
    number = abs(number)

    result = ""

    while number:

        number, remainder = divmod(number, base)
        result = DIGITS[remainder] + result

    if negative:
        result = "-" + result

    return result