from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t

def encode_twos(value: int, width: int) -> str:
    if width <= 0 or width > 1024:
        raise ValueError(t("error.invalid_width"))
    minimum = -(1 << (width - 1))
    maximum = (1 << (width - 1)) - 1
    if not minimum <= value <= maximum:
        raise ValueError(t("error.twos_range").format(minimum=minimum, maximum=maximum))
    return format(value & ((1 << width) - 1), f"0{width}b")

def decode_twos(bits: str) -> int:
    bits = bits.strip().replace(" ", "")
    if not bits or any(c not in "01" for c in bits):
        raise ValueError(t("error.invalid_binary"))
    width = len(bits)
    value = int(bits, 2)
    return value - (1 << width) if bits[0] == "1" else value

def twos_complement_menu():
    title(t("twos.title"))
    try:
        console.print(f"[cyan]1.[/] {t('twos.encode')}\n[cyan]2.[/] {t('twos.decode')}")
        mode = Prompt.ask(t("choose"))
        if mode == "1":
            value = int(Prompt.ask(t("twos.number")))
            width = int(Prompt.ask(t("bitrep.width")))
            console.print(f"[bold green]{encode_twos(value, width)}[/]")
        elif mode == "2":
            console.print(f"[bold green]{decode_twos(Prompt.ask(t('twos.bits')))}[/]")
        else:
            raise ValueError(t("error.invalid_choice"))
    except ValueError as e:
        error(str(e))
