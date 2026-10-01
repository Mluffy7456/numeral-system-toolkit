from converter import converter_menu
from calculator import calculator_menu
from bitwise import bitwise_menu
from truth_tables import truth_table_menu
from bit_representation import bit_representation_menu
from bit_grouping import bit_grouping_menu
from ieee754 import ieee754_menu
from ascii_converter import ascii_menu
from utf8_converter import utf8_menu
from twos_complement import twos_complement_menu
from gray_code import gray_menu
from history import show_history, clear_history
from config import APP_NAME, VERSION
from utils import clear_screen, logo
from rich_utils import console, title, pause, error, success
from language import load_language, t
from settings_menu import settings_menu

def run_action(action):
    action()
    pause(t("pause"))

def main():
    load_language()
    while True:
        clear_screen()
        logo()
        title(f"{APP_NAME} v{VERSION}")
        items = [
            ("1", "menu.converter"), ("2", "menu.calculator"), ("3", "menu.bitwise"),
            ("4", "menu.truth_tables"), ("5", "menu.bit_representation"), ("6", "menu.bit_grouping"),
            ("7", "menu.ieee754"), ("8", "menu.ascii"), ("9", "menu.utf8"),
            ("10", "menu.twos"), ("11", "menu.gray"), ("12", "menu.history"),
            ("13", "menu.clear_history"), ("14", "menu.settings"), ("15", "menu.gui"),
            ("0", "menu.exit")
        ]
        for number, key in items:
            console.print(f"[cyan]{number}.[/] {t(key)}")
        choice = console.input(f"\n[bold cyan]{t('choose')} > [/]").strip()
        actions = {
            "1": converter_menu, "2": calculator_menu, "3": bitwise_menu,
            "4": truth_table_menu, "5": bit_representation_menu, "6": bit_grouping_menu,
            "7": ieee754_menu, "8": ascii_menu, "9": utf8_menu,
            "10": twos_complement_menu, "11": gray_menu,
            "12": show_history, "13": clear_history
        }
        if choice in actions:
            run_action(actions[choice])
        elif choice == "14":
            settings_menu()
            load_language()
        elif choice == "15":
            try:
                from gui import run_gui
                run_gui()
            except Exception as exc:
                error(str(exc))
                pause(t("pause"))
        elif choice == "0":
            success(t("goodbye"))
            break
        else:
            error(t("error.invalid_choice"))
            pause(t("pause"))

if __name__ == "__main__":
    main()
