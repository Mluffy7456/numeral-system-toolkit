from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t

def text_to_utf8(text: str) -> str:
    return text.encode("utf-8").hex(" ").upper()

def utf8_to_text(value: str) -> str:
    try:
        return bytes.fromhex(value.replace(" ", "")).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        raise ValueError(t("error.invalid_utf8"))

def utf8_menu():
    title(t("utf8.title"))
    try:
        console.print(f"[cyan]1.[/] {t('utf8.encode')}\n[cyan]2.[/] {t('utf8.decode')}")
        mode = Prompt.ask(t("choose"))
        if mode == "1":
            console.print(f"[bold green]{text_to_utf8(Prompt.ask(t('utf8.text')))}[/]")
        elif mode == "2":
            console.print(f"[bold green]{utf8_to_text(Prompt.ask(t('utf8.bytes')))}[/]")
        else:
            raise ValueError(t("error.invalid_choice"))
    except ValueError as e:
        error(str(e))
