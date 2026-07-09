from converter import from_decimal


def show_representations(number: int, bit_width=None):

    binary = from_decimal(number, 2)

    if bit_width:
        binary = binary.zfill(bit_width)

    print("\n" + "=" * 50)
    print("Representations".center(50))
    print("=" * 50)

    print(f"Binary      : {binary}")
    print(f"Octal       : {from_decimal(number, 8)}")
    print(f"Decimal     : {number}")
    print(f"Hexadecimal : {from_decimal(number, 16)}")

    print("=" * 50)