from converter import converter_menu
from calculator import calculator_menu
from bitwise import bitwise_menu
from truth_tables import truth_table_menu
from bit_representation import bit_representation_menu
from bit_grouping import bit_grouping_menu
from history import show_history, clear_history
from config import APP_NAME, VERSION
from utils import clear_screen, logo
from rich_utils import console, title, pause, error, success
from language import load_language, t
from settings_menu import settings_menu

def main():
    load_language()
    while True:
        clear_screen()
        logo()
        title(f"{APP_NAME} v{VERSION}")
        console.print(f"[cyan]1.[/] {t('menu.converter')}")
        console.print(f"[cyan]2.[/] {t('menu.calculator')}")
        console.print(f"[cyan]3.[/] {t('menu.bitwise')}")
        console.print(f"[cyan]4.[/] {t('menu.truth_tables')}")
        console.print(f"[cyan]5.[/] {t('menu.bit_representation')}")
        console.print(f"[cyan]6.[/] {t('menu.bit_grouping')}")
        console.print(f"[cyan]7.[/] {t('menu.history')}")
        console.print(f"[cyan]8.[/] {t('menu.clear_history')}")
        console.print(f"[cyan]9.[/] {t('menu.settings')}")
        console.print(f"[cyan]0.[/] {t('menu.exit')}")
        choice = console.input(f"\n[bold cyan]{t('choose')} > [/]").strip()
        if choice == "1": converter_menu(); pause(t("pause"))
        elif choice == "2": calculator_menu(); pause(t("pause"))
        elif choice == "3": bitwise_menu(); pause(t("pause"))
        elif choice == "4": truth_table_menu(); pause(t("pause"))
        elif choice == "5": bit_representation_menu(); pause(t("pause"))
        elif choice == "6": bit_grouping_menu(); pause(t("pause"))
        elif choice == "7": show_history(); pause(t("pause"))
        elif choice == "8": clear_history(); pause(t("pause"))
        elif choice == "9": settings_menu(); load_language()
        elif choice == "0": success(t("goodbye")); break
        else: error(t("error.invalid_choice")); pause(t("pause"))

if __name__ == "__main__":
    main()
