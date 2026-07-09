from converter import converter_menu
from calculator import calculator_menu
from bitwise import bitwise_menu
from history import show_history, clear_history

from config import APP_NAME, VERSION

from utils import clear_screen, logo
from rich_utils import console, title, pause, error, success


def main():

    while True:

        clear_screen()

        logo()

        title(f"{APP_NAME} v{VERSION}")

        console.print("[cyan]1.[/] Number Converter")
        console.print("[cyan]2.[/] Calculator")
        console.print("[cyan]3.[/] Bitwise Operations")
        console.print("[cyan]4.[/] View History")
        console.print("[cyan]5.[/] Clear History")
        console.print("[cyan]6.[/] Exit")

        choice = console.input("\n[bold cyan]Choose > [/]").strip()

        if choice == "1":
            converter_menu()
            pause()

        elif choice == "2":
            calculator_menu()
            pause()

        elif choice == "3":
            bitwise_menu()
            pause()

        elif choice == "4":
            show_history()
            pause()

        elif choice == "5":
            clear_history()
            success("History cleared.")
            pause()

        elif choice == "6":
            success("Goodbye!")
            break

        else:
            error("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()