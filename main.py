from utils import clear_screen
from converter import converter_menu
from calculator import calculator_menu
from config import APP_NAME, VERSION
from utils import clear_screen, header, pause, logo
from history import show_history, clear_history
from bitwise import bitwise_menu


def main():

    while True:

        clear_screen()

        logo()
        
        print("=" * 45)
        print(f"{APP_NAME} v{VERSION}".center(45))
        print("=" * 45)

        print("1. Number Converter")
        print("2. Calculator")
        print("3. Bitwise Operations")
        print("4. View History")
        print("5. Clear History")
        print("6. Exit")

        choice = input("\nChoose: ")

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
            pause()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")
            pause()


if __name__ == "__main__":
    main()