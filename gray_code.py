from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t

def encode_gray(value: int) -> int:
    if value < 0:
        raise ValueError(t("error.gray_nonnegative"))
    return value ^ (value >> 1)

def decode_gray(gray: int) -> int:
    if gray < 0:
        raise ValueError(t("error.gray_nonnegative"))
    value = 0
    while gray:
        value ^= gray
        gray >>= 1
    return value

def gray_menu():
    title(t("gray.title"))
    try:
        console.print(f"[cyan]1.[/] {t('gray.encode')}\n[cyan]2.[/] {t('gray.decode')}")
        mode = Prompt.ask(t("choose"))
        value = int(Prompt.ask(t("gray.number")))
        if mode == "1":
            result = encode_gray(value)
        elif mode == "2":
            result = decode_gray(value)
        else:
            raise ValueError(t("error.invalid_choice"))
        console.print(f"[bold green]{result}[/]")
    except ValueError as e:
        error(str(e))
