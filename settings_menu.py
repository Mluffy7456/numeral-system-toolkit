from rich.prompt import Prompt

from rich_utils import (
    console,
    title,
    success,
    error
)

from language import (
    load_language,
    t
)

from settings import (
    get_language,
    set_language
)


def settings_menu():

    while True:

        title(t("settings.title"))

        current = get_language().upper()

        console.print(
            f"[green]{t('settings.current_language')}:[/] {current}"
        )

        console.print()

        console.print("[cyan]1.[/] English")
        console.print("[cyan]2.[/] Русский")
        console.print("[cyan]0.[/] Back")

        choice = Prompt.ask(
            t("choose")
        ).strip()

        if choice == "1":

            set_language("en")
            load_language()

            success("settings.saved")

        elif choice == "2":

            set_language("ru")
            load_language()

            success("settings.saved")

        elif choice == "0":

            return

        else:

            error("error.invalid_choice")