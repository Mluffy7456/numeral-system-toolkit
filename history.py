import json
from pathlib import Path
from datetime import datetime

from rich.table import Table
from rich import box

from rich_utils import console, success
from language import t


BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = BASE_DIR / "history.json"


def load_history():

    if not HISTORY_FILE.exists():
        return []

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_history(history):

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_converter_record(number, from_base, to_base, result):

    history = load_history()

    history.append({

        "type": "converter",

        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "number": number,

        "from_base": from_base,

        "to_base": to_base,

        "result": result

    })

    save_history(history)


def add_calculator_record(
    first_number,
    second_number,
    operation,
    base,
    result,
    decimal_result
):

    history = load_history()

    history.append({

        "type": "calculator",

        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "base": base,

        "first_number": first_number,

        "second_number": second_number,

        "operation": operation,

        "result": result,

        "decimal_result": decimal_result

    })

    save_history(history)


def add_bitwise_record(
    operation,
    first_number,
    second_number,
    base,
    result,
    shift=None
):

    history = load_history()

    record = {

        "type": "bitwise",

        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "base": base,

        "operation": operation,

        "first_number": first_number,

        "second_number": second_number,

        "result": result

    }

    if shift is not None:
        record["shift"] = shift

    history.append(record)

    save_history(history)


def show_history():

    history = load_history()

    if not history:

        console.print(
            f"[yellow]{t('history.empty')}[/]"
        )
        return

    table = Table(
        title=t("history.title"),
        box=box.ROUNDED,
        header_style="bold cyan"
    )

    table.add_column(
        t("history.time"),
        style="green"
    )

    table.add_column(
        t("history.type"),
        style="cyan"
    )

    table.add_column(
        t("history.operation")
    )

    table.add_column(
        t("history.result"),
        style="yellow"
    )

    for record in history:

        if record["type"] == "converter":

            operation = (
                f"{record['number']} "
                f"({record['from_base']} → {record['to_base']})"
            )

        elif record["type"] == "calculator":

            operation = (
                f"{record['first_number']} "
                f"{record['operation']} "
                f"{record['second_number']}"
            )

        else:

            operation = (
                f"{record['operation']} "
                f"{record['first_number']}"
            )

            if record.get("second_number") != "-":

                operation += (
                    f" {record['second_number']}"
                )

            if "shift" in record:

                operation += (
                    f" ({record['shift']})"
                )

        table.add_row(

            record["timestamp"],

            record["type"].capitalize(),

            operation,

            record["result"]

        )

    console.print()
    console.print(table)


def clear_history():

    save_history([])

    success("history.cleared")