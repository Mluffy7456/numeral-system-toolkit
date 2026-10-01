import struct
from rich.prompt import Prompt
from rich.table import Table
from rich_utils import console, title, error
from language import t

FORMATS = {"1": (32, ">f", ">I"), "2": (64, ">d", ">Q")}

def encode_float(value: float, bits: int):
    fmt = ">f" if bits == 32 else ">d"
    raw = struct.pack(fmt, value)
    integer = int.from_bytes(raw, "big")
    binary = format(integer, f"0{bits}b")
    sign = binary[0]
    exponent_bits = 8 if bits == 32 else 11
    fraction_bits = bits - exponent_bits - 1
    exponent = binary[1:1 + exponent_bits]
    fraction = binary[1 + exponent_bits:]
    return sign, exponent, fraction, binary, f"{integer:0{bits // 4}X}"

def decode_float(raw: str, bits: int) -> float:
    raw = raw.strip().replace(" ", "").replace("_", "")
    if len(raw) == bits and set(raw) <= {"0", "1"}:
        integer = int(raw, 2)
    elif len(raw) == bits // 4:
        integer = int(raw, 16)
    else:
        raise ValueError(t("error.invalid_ieee"))
    return struct.unpack(">f" if bits == 32 else ">d", integer.to_bytes(bits // 8, "big"))[0]

def ieee754_menu():
    title(t("ieee.title"))
    try:
        console.print("[cyan]1.[/] IEEE 754 binary32 (32-bit)\n[cyan]2.[/] IEEE 754 binary64 (64-bit)")
        choice = Prompt.ask(t("choose"))
        if choice not in FORMATS:
            raise ValueError(t("error.invalid_choice"))
        bits = FORMATS[choice][0]
        console.print(f"[cyan]1.[/] {t('ieee.encode')}\n[cyan]2.[/] {t('ieee.decode')}")
        mode = Prompt.ask(t("choose"))
        if mode == "1":
            value = float(Prompt.ask(t("ieee.number")))
            sign, exponent, fraction, binary, hexadecimal = encode_float(value, bits)
            table = Table(title=t("ieee.result"), header_style="bold cyan")
            table.add_column(t("ieee.field")); table.add_column(t("ieee.value"))
            table.add_row(t("ieee.sign"), sign)
            table.add_row(t("ieee.exponent"), exponent)
            table.add_row(t("ieee.fraction"), fraction)
            table.add_row(t("ieee.binary"), f"{sign} {exponent} {fraction}")
            table.add_row(t("ieee.hex"), hexadecimal)
            console.print(table)
        elif mode == "2":
            raw = Prompt.ask(t("ieee.raw"))
            console.print(f"[bold green]{t('ieee.number')}[/]: {decode_float(raw, bits)!r}")
        else:
            raise ValueError(t("error.invalid_choice"))
    except (ValueError, OverflowError) as e:
        error(str(e))
