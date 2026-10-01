from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t

def text_to_ascii(text: str) -> str:
    if any(ord(c) > 127 for c in text):
        raise ValueError(t("error.ascii_only"))
    return " ".join(str(ord(c)) for c in text)

def ascii_to_text(value: str) -> str:
    try:
        nums = [int(x) for x in value.replace(",", " ").split()]
        if any(n < 0 or n > 127 for n in nums):
            raise ValueError
        return "".join(chr(n) for n in nums)
    except ValueError:
        raise ValueError(t("error.invalid_ascii"))

def ascii_menu():
    title(t("ascii.title"))
    try:
        console.print(f"[cyan]1.[/] {t('ascii.encode')}\n[cyan]2.[/] {t('ascii.decode')}")
        mode = Prompt.ask(t("choose"))
        if mode == "1":
            text = Prompt.ask(t("ascii.text"))
            console.print(f"[bold green]{text_to_ascii(text)}[/]")
        elif mode == "2":
            value = Prompt.ask(t("ascii.codes"))
            console.print(f"[bold green]{ascii_to_text(value)}[/]")
        else:
            raise ValueError(t("error.invalid_choice"))
    except ValueError as e:
        error(str(e))
