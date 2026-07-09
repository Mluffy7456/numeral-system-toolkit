import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("history.json")


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


def add_calculator_record(first_number,
                          second_number,
                          operation,
                          base,
                          result,
                          decimal_result):

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


def show_history():

    history = load_history()

    if not history:

        print("\nHistory is empty.")
        return

    print("\n========== HISTORY ==========\n")

    for record in history:

        print(f"Time : {record['timestamp']}")
        print(f"Type : {record['type']}")

        if record["type"] == "converter":

            print(
                f"{record['number']} "
                f"(base {record['from_base']}) "
                f"→ base {record['to_base']}"
            )

            print(f"Result : {record['result']}")
            
        elif record["type"] == "bitwise":

            print(
                f"{record['first_number']} "
                f"{record['operation']} "
                f"{record['second_number']}"
            )

            print(f"Base : {record['base']}")
            print(f"Result : {record['result']}")

        else:

            print(
                f"{record['first_number']} "
                f"{record['operation']} "
                f"{record['second_number']}"
            )

            print(f"Base : {record['base']}")
            print(f"Result : {record['result']}")
            print(f"Decimal : {record['decimal_result']}")

        print("-" * 50)

def add_bitwise_record(operation,
                       first_number,
                       second_number,
                       base,
                       result):

    history = load_history()

    history.append({

        "type": "bitwise",

        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "base": base,

        "operation": operation,

        "first_number": first_number,

        "second_number": second_number,

        "result": result

    })

    save_history(history)

def clear_history():

    save_history([])

    print("\nHistory cleared.")