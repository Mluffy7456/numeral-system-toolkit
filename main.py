from utils import clear_screen
from converter import converter_menu
from calculator import calculator_menu
from config import APP_NAME, VERSION
from utils import clear_screen, header, pause, logo


def main():

    while True:

        clear_screen()

        header()
        logo()
        
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
            pause()

        elif choice == "2":
            calculator_menu()
            pause()

        elif choice == "3":
            print("\nHistory is empty.")
            pause()

        elif choice == "4":
            print("\nHistory module is not implemented yet.")
            pause()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")
            pause()


if __name__ == "__main__":
    main()