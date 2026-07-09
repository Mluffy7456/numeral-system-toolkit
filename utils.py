import os

from config import APP_NAME, VERSION, LINE


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    print(r"""
███╗   ██╗███████╗████████╗
████╗  ██║██╔════╝╚══██╔══╝
██╔██╗ ██║███████╗   ██║
██║╚██╗██║╚════██║   ██║
██║ ╚████║███████║   ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝

    Numeral System Toolkit - by Mluffy
""")
    
def header():

    print(LINE)
    print(f"{APP_NAME} v{VERSION}".center(50))
    print(LINE)


def pause():
    input("\nPress Enter to continue...")


def print_result(title, value):

    print("\n" + LINE)
    print(title.center(50))
    print(LINE)

    print(value)

    print(LINE)
    