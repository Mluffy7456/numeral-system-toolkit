from utils import clear_screen
from converter import converter_menu
from calculator import calculator_menu
from config import APP_NAME, VERSION


def main():

    while True:

        clear_screen()

        print("=" * 45)
        print(f"{APP_NAME} v{VERSION}".center(45))
        print("=" * 45)

        print("1. Number Converter")
        print("2. Calculator")
        print("3. View History")
        print("4. Clear History")
        print("5. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            converter_menu()
            input("\nPress Enter...")

        elif choice == "2":
            calculator_menu()
            input("\nPress Enter...")

        elif choice == "3":
            print("\nHistory module is not implemented yet.")
            input("\nPress Enter...")

        elif choice == "4":
            print("\nHistory module is not implemented yet.")
            input("\nPress Enter...")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")
            input("\nPress Enter...")


if __name__ == "__main__":
    main()